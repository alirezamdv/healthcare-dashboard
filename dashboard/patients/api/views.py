# [OWN_DD]
# Authors: Jennifer Horstmann, alma@uni-bremen.de

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework.permissions import BasePermission, SAFE_METHODS

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from background_task import background
from dashboard.patients.api.serializers import PatientSerializer, ReportSerializer, ReportHistorySerializer, \
    DengueSerializer, DiagnosisSerializers

from dashboard.patients.models import Patient, Report, Dengue, Diagnosis
import dateutil.parser
from datetime import timedelta, datetime

from background_task.models import Task
from django.utils import timezone





class Isstaff(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='staff') or request.user.is_superuser:
            return True
        return False


# @permission_required("auth.add_patients")
class PatientViewSet(ModelViewSet):
    """
    This view returns a list of all patients in the systems
    ordered by their admission date.
    """

    # permission_required = "patients.change_patients"
    # permission_classes = [PostPermission]
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['diagnosis__status', 'diagnosis__disease_type', 'first_name', 'last_name', 'gender',
                     'admission_date',"admission_number","hospital_number",
                     "patientId"]

    def get_queryset(self):
        queryset = Patient.objects.all()
        queryset = queryset.order_by('-admission_date')
        return queryset

    def get_permissions(self, *args, **kwargs):
        if self.request.method == "GET":
            self.permission_classes = [permissions.IsAuthenticated]
        if self.request.method == "POST" or self.request.method == "PATCH" or \
            self.request.method == "PUT" or self.request.method == "DELETE":
            self.permission_classes = [Isstaff]
        return super(PatientViewSet, self).get_permissions()


class ReportViewSet(ModelViewSet):
    """
    This view returns a list of all reports and their respective histories in the system.
    The reports can be filtered by their status with a query in the url like so:
    /api/reports/?status=ok
    """
    serializer_class = ReportSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def get_queryset(self):
        queryset = Report.objects.all()
        queryset_history = Report.history.model.objects.all()
        patient = self.request.query_params.get('patient', None)
        if patient is not None:
            queryset = queryset.filter(patient=patient)
            queryset = queryset.order_by('-id')
        return queryset

    def get_permissions(self, *args, **kwargs):
        if self.request.method == "GET":
            self.permission_classes = [permissions.IsAuthenticated]
        if self.request.method == "POST" or self.request.method == "patch" or \
            self.request.method == "PUT" or self.request.method == "DELETE":
            self.permission_classes = [Isstaff]
        return super(ReportViewSet, self).get_permissions()


class ReportHistoryViewSet(ModelViewSet):
    """
    This view returns a list of all history objects in the system.
    """
    queryset = Report.history.model.objects.all()
    serializer_class = ReportHistorySerializer
    lookup_field = 'history_id'


class DengueViewSet(ModelViewSet):
    serializer_class = DengueSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['patient']

    def get_queryset(self):
        queryset = Dengue.objects.all()
        patient = self.request.query_params.get('patient', None)
        if patient is not None:
            queryset = queryset.filter(patient=patient)
            queryset = queryset.order_by('-id')
        return queryset

    def get_permissions(self, *args, **kwargs):
        if self.request.method == "GET":
            self.permission_classes = [permissions.IsAuthenticated]
        if self.request.method == "POST" or self.request.method == "patch" or \
            self.request.method == "PUT" or self.request.method == "DELETE":
            self.permission_classes = [Isstaff]
        return super(DengueViewSet, self).get_permissions()

class DiagnosisViewSet(ModelViewSet):
    serializer_class = DiagnosisSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['patient']

    def get_queryset(self):
        queryset = Diagnosis.objects.all()
        patient = self.request.query_params.get('patient', None)
        if patient is not None:
            queryset = queryset.filter(patient=patient)
            queryset = queryset.order_by('-id')
        return queryset

    def get_permissions(self, *args, **kwargs):
        if self.request.method == "GET":
            self.permission_classes = [permissions.IsAuthenticated]
        if self.request.method == "POST" or self.request.method == "patch" or \
            self.request.method == "PUT" or self.request.method == "DELETE":
            self.permission_classes = [Isstaff]
        return super(DiagnosisViewSet, self).get_permissions()


@background(remove_existing_tasks=True)
def calc_fever(message):
    instance = Report.objects.get(id=message['id'])
    serializer = ReportSerializer(instance).data
    channel_layer = get_channel_layer()

    if len(serializer['history']) > 2:

        sorted_obj = dict(serializer)
        sorted_obj['history'] = sorted(serializer['history'], key=lambda x: x['datetime'], reverse=False)

        unique = []
        for entry in sorted_obj['history']:
            date = dateutil.parser.parse(entry['datetime']).date()
            if date in unique:
                continue
            else:
                unique.append(date)

        if len(unique) > 2:
            con_days = []
            con_days.append(unique[0])
            for date in unique[1:]:
                if (date - timedelta(days=1)) in unique:
                    con_days.append(date)

            if len(con_days) >= 2:
                fever_days = []
                for day in con_days:
                    filtered_days = [obj for obj in sorted_obj['history'] if
                                     (dateutil.parser.parse(obj['datetime']).date() == day)]
                    max_fever = max([obj['fever'] for obj in filtered_days])
                    max_fever_day = [obj for obj in filtered_days if (max(obj['fever']))]
                    fever_days.append(max_fever_day[0])

                current_day = [obj for obj in sorted_obj['history'] if
                               (dateutil.parser.parse(obj['datetime']).date() == unique[-1:][0])]
                if all([float(entry['fever']) >= 38.0 for entry in fever_days[:-1]]) and float(
                    current_day[0]['fever']) <= 37.5:
                    async_to_sync(channel_layer.group_send)(
                        "history", {"type": "notify.me",
                                    "text": message,
                                    "report": serializer,
                                    "reason": "fever"
                                    }
                    )


@background(remove_existing_tasks=True)
def notify_user(message):
    instance = Report.objects.get(id=message['id'])
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        "history", {"type": "notify.me",
                    "text": message,
                    "report": ReportSerializer(instance).data,
                    "reason": "interval"
                    }
    )
