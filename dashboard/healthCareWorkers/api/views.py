# [OWN_DD]
# Authors: Jennifer Horstmann, alma@uni-bremen.de
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from dashboard.healthCareWorkers.api.serializers import HealthCareWorkerSerializer, CaseSerializer, \
    HealthcareDepartmentSerializer, AddressSerializer
from dashboard.healthCareWorkers.models import HealthCareDepartment, HealthCareWorker, Case, Address


class IsHcw(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='hcw') or request.user.is_superuser:
            return True
        return False


class HealthCareDepartmentViewSet(ModelViewSet):
    """
    This view returns a list of all HCW-Departments
    """
    serializer_class = HealthcareDepartmentSerializer

    def get_queryset(self):
        queryset = HealthCareDepartment.objects.all()
        # patient = self.request.query_params.get('patient', None)
        # if patient is not None:
        #     queryset = queryset.filter(patient=patient)
        #     queryset = queryset.order_by('-id')
        return queryset

    def get_permissions(self, *args, **kwargs):
        if self.request.method == "GET":
            self.permission_classes = [permissions.IsAuthenticated]
        if self.request.method == "POST" or self.request.method == "patch" or \
            self.request.method == "PUT" or self.request.method == "DELETE":
            self.permission_classes = [IsHcw]
        return super(HealthCareDepartmentViewSet, self).get_permissions()


class HealthCareWorkerViewSet(ModelViewSet):
    """
    This view returns a list of all HCW-Departments
    """
    serializer_class = HealthCareWorkerSerializer

    def get_queryset(self):
        queryset = HealthCareWorker.objects.all()
        # patient = self.request.query_params.get('patient', None)
        # if patient is not None:
        #     queryset = queryset.filter(patient=patient)
        #     queryset = queryset.order_by('-id')
        return queryset

    def get_permissions(self, *args, **kwargs):
        if self.request.method == "GET":
            self.permission_classes = [permissions.IsAuthenticated]
        if self.request.method == "POST" or self.request.method == "patch" or \
            self.request.method == "PUT" or self.request.method == "DELETE":
            self.permission_classes = [IsHcw]
        return super(HealthCareWorkerViewSet, self).get_permissions()


class CaseViewSet(ModelViewSet):
    """
    This view returns a list of all HCW-Departments
    """
    serializer_class = CaseSerializer

    def get_queryset(self):
        queryset = Case.objects.all()
        # patient = self.request.query_params.get('patient', None)
        # if patient is not None:
        #     queryset = queryset.filter(patient=patient)
        #     queryset = queryset.order_by('-id')
        return queryset

    def get_permissions(self, *args, **kwargs):
        if self.request.method == "GET":
            self.permission_classes = [permissions.IsAuthenticated]
        if self.request.method == "POST" or self.request.method == "patch" or \
            self.request.method == "PUT" or self.request.method == "DELETE":
            self.permission_classes = [IsHcw]
        return super(CaseViewSet, self).get_permissions()


class AddressViewSet(ModelViewSet):
    """
    This view returns a list of all locations
    """
    serializer_class = AddressSerializer

    def get_queryset(self):
        queryset = Address.objects.all()
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
            self.permission_classes = [IsHcw]
        return super(AddressViewSet, self).get_permissions()


# class NotificationsViewSet(ModelViewSet):
#     serializer_class = NotificationSerializer
#
#     def get_queryset(self):
#         queryset = Notification.objects.all()
#         case = self.request.query_params.get('case', None)
#         if case is not None:
#             queryset = queryset.filter(case=case)
#             queryset = queryset.order_by('-id')
#         return queryset
#
#     def get_permissions(self, *args, **kwargs):
#         if self.request.method == "GET":
#             self.permission_classes = [permissions.IsAuthenticated]
#         if self.request.method == "POST" or self.request.method == "patch" or \
#             self.request.method == "PUT" or self.request.method == "DELETE":
#             self.permission_classes = [IsHcw]
#         return super(NotificationsViewSet, self).get_permissions()
