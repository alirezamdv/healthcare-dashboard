# [OWN_DD]
# Author: Alma@uni-bremen.de

from asgiref.sync import sync_to_async
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

from dashboard.healthCareWorkers.api.serializers import HealthCareWorkerSerializer, CaseSerializer, \
    HealthcareDepartmentSerializer,AddressSerializer
from dashboard.patients.api.views import notify_user, calc_fever
from dashboard.healthCareWorkers.models import HealthCareDepartment, HealthCareWorker, Case,Address

class IsHcw(permissions.BasePermission):
    message = "you do not have permissions to perform this Action."

    def has_permission(self, **kwargs):
        scope = kwargs.pop("scope")
        if scope['user'] and scope['user'].groups.filter(name='hcw') or scope['user'].is_superuser:
            return True
        return False
# class HealthCareDepartmentConsumerObserver(AsyncAPIConsumer):
#     async def accept(self, **kwargs):
#         await super().accept(**kwargs)
#
#
#     @model_observer(Locations)
#     async def report_change(self, message, **kwargs):
#         print(message)
#         await self.send_json(message)
#
#     def get_report(self, message, **kwargs):
#         return (Report.objects.get)(pk=message['pk'])


class HealthcareWorkerConsumer(ObserverModelInstanceMixin, ListModelMixin, RetrieveModelMixin, PatchModelMixin,
                               CreateModelMixin,
                               UpdateModelMixin,
                               DeleteModelMixin, GenericAsyncAPIConsumer, AsyncAPIConsumer):
    queryset = HealthCareWorker.objects.all()
    serializer_class = HealthCareWorkerSerializer

    def get_permissions(self, action, *args, **kwargs):
        if action == "list":
            self.permission_classes = [permissions.IsAuthenticated]
        if action == "create" or action == "patch" or action == "delete" or action == "change":
            self.permission_classes = [IsHcw]
        return super(HealthcareWorkerConsumer, self).get_permissions(action)


class HealthcareDepartmentConsumer(ObserverModelInstanceMixin, ListModelMixin, RetrieveModelMixin, PatchModelMixin,
                                   CreateModelMixin,
                                   UpdateModelMixin,
                                   DeleteModelMixin, GenericAsyncAPIConsumer, AsyncAPIConsumer):
    queryset = HealthCareDepartment.objects.all()
    serializer_class = HealthcareDepartmentSerializer

    def get_permissions(self, action, *args, **kwargs):
        if action == "list":
            self.permission_classes = [permissions.IsAuthenticated]
        if action == "create" or action == "patch" or action == "delete" or action == "change":
            self.permission_classes = [IsHcw]
        return super(HealthcareDepartmentConsumer, self).get_permissions(action)


class CaseConsumer(ObserverModelInstanceMixin, ListModelMixin, RetrieveModelMixin, PatchModelMixin, CreateModelMixin,
                   UpdateModelMixin,
                   DeleteModelMixin, GenericAsyncAPIConsumer, AsyncAPIConsumer):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    def get_permissions(self, action, *args, **kwargs):
        if action == "list":
            self.permission_classes = [permissions.IsAuthenticated]
        if action == "create" or action == "patch" or action == "delete" or action == "change":
            self.permission_classes = [IsHcw]
        return super(CaseConsumer, self).get_permissions(action)

# class AddressConsumerObserver(AsyncAPIConsumer):
#     async def accept(self, **kwargs):
#         await super().accept(**kwargs)
#         await self.report_change.subscribe()
#
#     @model_observer(Address)
#     async def report_change(self, message, **kwargs):
#         print(message)
#         await self.send_json(message)
#
#     def get_report(self, message, **kwargs):
#         return (Report.objects.get)(pk=message['pk'])


class AddressConsumer(ObserverModelInstanceMixin, ListModelMixin, RetrieveModelMixin, PatchModelMixin, CreateModelMixin,
                      UpdateModelMixin,
                      DeleteModelMixin, GenericAsyncAPIConsumer, AsyncAPIConsumer):
    # queryset = Report.objects.all()
    serializer_class = AddressSerializer
    def get_permissions(self, action, *args, **kwargs):
        if action == "list":
            self.permission_classes = [permissions.IsAuthenticated]
        if action == "create" or action == "patch" or action == "delete" or action == "change":
            self.permission_classes = [IsHcw]
        return super(AddressConsumer, self).get_permissions(action)
