# [OWN_DD]
# Author: alma@uni-bremen.de

from rest_framework import serializers, fields

from dashboard.healthCareWorkers.models import HealthCareWorker, HealthCareDepartment, Case, Address, ADDRESS_CAT
from dashboard.patients.models import Patient, Diagnosis
from dashboard.patients.api.serializers import DiagnosisSerializers


# class CustomMultipleChoiceField(fields.MultipleChoiceField):
#     def to_representation(self, value):
#         return list(super().to_representation(value))


class AddressSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)
    patient_id = serializers.IntegerField(write_only=True)
    # category = CustomMultipleChoiceField(choices=ADDRESS_CAT)

    class Meta:
        model = Address
        fields = "__all__"


# class NotificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Notification
#         fields = "__all__"  # ["case", "HealthCareDepartment", "note", "notificationDate", "created_at", "updated_at"]
#

class HealthCareWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCareWorker
        fields = "__all__"


class HealthcareDepartmentSerializer(serializers.ModelSerializer):
    healthcareWorkers = HealthCareWorkerSerializer(many=True, read_only=True)

    class Meta:
        model = HealthCareDepartment
        fields = ["name", "contact_email", "healthcareWorkers", "created_at", "updated_at", "changed_by"]


class CaseSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)
    patient_id = serializers.IntegerField(write_only=True)
    admission_date = serializers.DateTimeField(source='patient.admission_date', read_only=True)
    dismissal_date = serializers.DateTimeField(source='patient.dismissal_date', read_only=True)
    diagnosis = serializers.SerializerMethodField('get_diagnosis')
    addresses = serializers.SerializerMethodField('get_addresses')

    class Meta:
        model = Case
        fields = "__all__"

    def get_diagnosis(self, case):
        qs = Diagnosis.objects.filter(patient__in=Patient.objects.filter(pk=case.patient.id)).last()
        serializer = DiagnosisSerializers(instance=qs)
        return serializer.data

    def get_addresses(self, case):
        qs = Address.objects.filter(patient__in=Patient.objects.filter(pk=case.patient.id))
        serializer = AddressSerializer(instance=qs, many=True)
        return serializer.data


''
