# [OWN_DD]
# Authors: Jennifer Horstmann, alma@uni-bremen.de

from asgiref.sync import sync_to_async
from django.contrib.auth.mixins import PermissionRequiredMixin
from djangochannelsrestframework import permissions
from djangochannelsrestframework.consumers import AsyncAPIConsumer
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    PatchModelMixin,
    DeleteModelMixin,
    CreateModelMixin,
)
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin
from djangochannelsrestframework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

from dashboard.patients.api.serializers import PatientSerializer, ReportSerializer, ReportHistorySerializer, \
    DengueSerializer, DiagnosisSerializers
from dashboard.patients.api.views import notify_user, calc_fever
from dashboard.patients.models import Patient, Report, Dengue, Diagnosis

import dateutil.parser
from datetime import timedelta, datetime, timezone
from django.utils.timezone import make_aware


class IsHcw(permissions.BasePermission):
    message = "you do not have permissions to perform this Action."

    def has_permission(self, **kwargs):
        scope = kwargs.pop("scope")
        if scope['user'] and scope['user'].groups.filter(name='hcw') or scope['user'].is_superuser:
            return True
        return False


class Isstaff(permissions.BasePermission):
    message = "you do not have permissions to perform this Action."

    def has_permission(self, **kwargs):
        scope = kwargs.pop("scope")
        print("scope", scope['user'], scope['user'].is_superuser)
        if scope['user'] and scope['user'].groups.filter(name='staff') or scope['user'].is_superuser:
            return True
        return False


class HistoryConsumerObserver(AsyncAPIConsumer):

    async def accept(self, **kwargs):
        await self.channel_layer.group_add(
            "history",
            self.channel_name
        )
        await super().accept(**kwargs)
        await self.history_change.subscribe()

    @model_observer(Report.history.model)
    async def history_change(self, message, **kwargs):
        """
        Observes changes of the history model instances.
        In case of a DELETE event the consumer is notified with an information about the deleted instance.
        In all other cases the consumer is notified about the update of the instance.
        If possible background tasks to send notifications are being triggered.
        :param message: The request/message from the consumer
        :param kwargs: Optional keyword arguments
        :return: The above stated websocket messages in json format to the consumer
        """
        if message['datetime'] and message['fever']:
            await sync_to_async(calc_fever)(message=message,
                                            schedule=(make_aware(datetime.now()) + timedelta(
                                                seconds=1)))

        if message['datetime'] and message['monitoring_interval']:
            time = message['datetime']
            interval = message['monitoring_interval']
            # TODO for demonstrating purposes minutes instead of hours
            schedule = dateutil.parser.parse(time) + timedelta(minutes=int(interval))
            # only send notifications that are scheduled for the future
            if schedule > datetime.now(timezone.utc):
                await sync_to_async(notify_user)(message=message, schedule=schedule)

        await self.send_json(message)

    @history_change.serializer
    def history_serializer(self, instance, action, **kwargs):
        """
        Serializes the history instance to be sent in json format to the consumer.
        :param instance: The history instance
        :param action: Create, update, patch, list, delete
        :param kwargs: Optional keyword arguments
        :return: The serialized history instance
        """
        return ReportHistorySerializer(instance).data

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("history", self.channel_name)
        await self.close()


class ReportConsumerObserver(AsyncAPIConsumer):
    async def accept(self, **kwargs):
        await super().accept(**kwargs)
        await self.report_change.subscribe()

    @model_observer(Report)
    async def report_change(self, message, **kwargs):
        await self.send_json(message)

    def get_report(self, message, **kwargs):
        return (Report.objects.get)(pk=message['pk'])


class PatientConsumerObserver(AsyncAPIConsumer):

    async def accept(self, **kwargs):
        await super().accept(**kwargs)
        await self.patient_change.subscribe()

    @model_observer(Patient)
    async def patient_change(self, message, **kwargs):
        """
        Observes changes of the patient model instances.
        :param message: The request/message from the consumer
        :param kwargs: Optional keyword arguments
        :return: Information about the change event via websocket messages in json format to the consumer
        """
        await self.send_json(message)

    @patient_change.serializer
    def patient_serializer(self, instance, action, **kwargs):
        """ Serializes the patient instance to be sent in json format to the consumer.
        :param instance: The patient instance
        :param action: Create, update, patch, list, delete
        :param kwargs: Optional keyword arguments
        :return: The serialized history instance
        """
        return PatientSerializer(instance).data


class PatientConsumer(ObserverModelInstanceMixin, ListModelMixin, RetrieveModelMixin, PatchModelMixin, UpdateModelMixin,
                      CreateModelMixin,
                      DeleteModelMixin, GenericAsyncAPIConsumer, PatientConsumerObserver, ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    # permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self, action, *args, **kwargs):
        if action == "list":
            self.permission_classes = [permissions.IsAuthenticated]
        if action == "create" or action == "patch" or action == "delete" or action == "change":
            self.permission_classes = [Isstaff]
        return super(PatientConsumer, self).get_permissions(action)


class ReportConsumer(ObserverModelInstanceMixin, ListModelMixin, RetrieveModelMixin, PatchModelMixin, CreateModelMixin,
                     UpdateModelMixin,
                     DeleteModelMixin, GenericAsyncAPIConsumer, AsyncAPIConsumer):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def get_permissions(self, action, *args, **kwargs):
        if action == "list":
            self.permission_classes = [permissions.IsAuthenticated]
        if action == "create" or action == "patch" or action == "delete" or action == "change":
            self.permission_classes = [Isstaff]
        return super(ReportConsumer, self).get_permissions(action)


class HistoryConsumer(ObserverModelInstanceMixin, ListModelMixin, RetrieveModelMixin, PatchModelMixin, UpdateModelMixin,
                      DeleteModelMixin, GenericAsyncAPIConsumer, HistoryConsumerObserver):
    queryset = Report.history.model.objects.all()
    serializer_class = ReportHistorySerializer

    def get_permissions(self, action, *args, **kwargs):
        if action == "list":
            self.permission_classes = [permissions.IsAuthenticated]
        if action == "create" or action == "patch" or action == "delete" or action == "change":
            self.permission_classes = [Isstaff]
        return super(HistoryConsumer, self).get_permissions(action)

    async def notify_me(self, event):
        """ Sends a notification to the websocket consumer.
        """
        await self.send_json(
            {"type": "notification", "data": {"patient": (event['text'])['patient'], "type": event['reason']}})


class DengueConsumerObserver(AsyncAPIConsumer):

    async def accept(self, **kwargs):
        await super().accept(**kwargs)
        await self.dengue_change.subscribe()

    @model_observer(Dengue)
    async def dengue_change(self, message, **kwargs):
        """
        Observes changes of the Dengue model instances.
        :param message: The request/message from the consumer
        :param kwargs: Optional keyword arguments
        :return: Information about the change event via websocket messages in json format to the consumer
        """
        await self.send_json(message)

    @dengue_change.serializer
    def dengue_serializer(self, instance, action, **kwargs):
        """ Serializes the patient instance to be sent in json format to the consumer.
        :param instance: The Dengue instance
        :param action: Create, update, patch, list, delete
        :param kwargs: Optional keyword arguments
        :return: The serialized history instance
        """
        return DengueSerializer(instance).data


class DengueConsumer(ObserverModelInstanceMixin, ListModelMixin, RetrieveModelMixin, PatchModelMixin, UpdateModelMixin,
                     CreateModelMixin,
                     DeleteModelMixin, GenericAsyncAPIConsumer, DengueConsumerObserver):
    queryset = Dengue.objects.all()
    serializer_class = DengueSerializer

    def get_permissions(self, action, *args, **kwargs):
        if action == "list":
            self.permission_classes = [permissions.IsAuthenticated]
        if action == "create" or action == "patch" or action == "delete" or action == "change":
            self.permission_classes = [Isstaff]
        return super(DengueConsumer, self).get_permissions(action)

    async def notify_me(self, event):
        """ Sends a notification to the websocket consumer.
        """
        await self.send_json(
            {"type": "notification", "data": {"patient": (event['text'])['patient'], "type": event['reason']}})


class DiagnosisConsumerObserver(AsyncAPIConsumer):

    async def accept(self, **kwargs):
        await super().accept(**kwargs)
        await self.diagnosis_change.subscribe()

    @model_observer(Diagnosis)
    async def diagnosis_change(self, message, **kwargs):
        """
        Observes changes of the Diagnosis model instances.
        :param message: The request/message from the consumer
        :param kwargs: Optional keyword arguments
        :return: Information about the change event via websocket messages in json format to the consumer
        """
        await self.send_json(message)

    @diagnosis_change.serializer
    def diagnosis_serializer(self, instance, action, **kwargs):
        """ Serializes the patient instance to be sent in json format to the consumer.
        :param instance: The Dengue instance
        :param action: Create, update, patch, list, delete
        :param kwargs: Optional keyword arguments
        :return: The serialized history instance
        """
        return DiagnosisSerializers(instance).data


class DiagnosisConsumer(ObserverModelInstanceMixin, ListModelMixin, RetrieveModelMixin, PatchModelMixin,
                        UpdateModelMixin,
                        CreateModelMixin,
                        DeleteModelMixin, GenericAsyncAPIConsumer, DiagnosisConsumerObserver):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializers

    # permission_classes = (permissions.IsAuthenticated,)
    def get_permissions(self, action, *args, **kwargs):
        if action == "list":
            self.permission_classes = [permissions.IsAuthenticated]
        if action == "create" or action == "patch" or action == "delete" or action == "change":
            self.permission_classes = [Isstaff]
        return super(DiagnosisConsumer, self).get_permissions(action)

    async def notify_me(self, event):
        """ Sends a notification to the websocket consumer.
        """
        await self.send_json(
            {"type": "notification", "data": {"patient": (event['text'])['patient'], "type": event['reason']}})
