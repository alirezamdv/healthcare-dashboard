# [OWN_DD]
# Authors: Jennifer Horstmann, alma@uni-bremen.de

from rest_framework import serializers, fields
from dashboard.patients.models import Patient, Report, Dengue, Diagnosis


#
# def required(value):
#     if len(value) < 1:
#         raise serializers.ValidationError('This field is required')


class ReportHistorySerializer(serializers.ModelSerializer):
    history_date = serializers.CharField(write_only=True)
    history_change_reason = serializers.CharField(write_only=True)
    history_type = serializers.CharField(write_only=True)
    history_relation = serializers.IntegerField(write_only=True)
    history_user_name = serializers.StringRelatedField(source='history_user', read_only=True)

    class Meta:
        model = Report.history.model
        fields = "__all__"


class ReportKeySerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(default=1)

    class Meta:
        model = Report
        fields = ["pk", ]


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id", "first_name", "last_name", "gender", "age", "patientId", "admission_number", "hospital_number",
                  "admission_date",
                  "dismissal_date", "updated_at", "created_at"]


class CustomListSerializer(fields.ListField):
    def to_representation(self, value):
        return list(super().to_representation(value))[-1]


class ReportSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)
    patient_id = serializers.IntegerField(write_only=True)
    patient_name = serializers.StringRelatedField(source='patient.name', read_only=True)
    admission_number = CustomListSerializer(source='patient.admission_number', read_only=True)
    history = ReportHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Report
        fields = ["pk", "patient", "admission_number", "patient_id", "patient_name", "daytime", "datetime",
                  "day_of_fever", "fever",
                  "pulse", "respiration", "bp_sys",
                  "bp_dia",
                  "fluid_input", "fi_oral", "fi_parenteral", "fi_other", "fi_eight_hrs", "fi_total", "fluid_output",
                  "fo_urine", "fo_uf", "fo_emesis", "fo_drainage",
                  "fo_eight_hrs", "fo_total", "diet", "pain_score", "abd_cir", "stools", "urine", "weight_ht", "weight",
                  "height", "o2sat", "additional", "status",
                  "status_changed_to_critical", "monitoring_interval", "history", "created_at", "updated_at",
                  "changed_by", "medical_advice", "hematocrit", "platelet", "wbc", "warning_signs",
                  ]


class CustomMultipleChoiceField(fields.MultipleChoiceField):
    def to_representation(self, value):
        return list(super().to_representation(value))


class DengueSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)
    patient_id = serializers.IntegerField(write_only=True)
    patient_name = serializers.StringRelatedField(source='patient', read_only=True)
    patient_gender = serializers.StringRelatedField(source='patient.gender', read_only=True)

    # bleeding_categories = BleedingCategory  # fields.MultipleChoiceField(choices=BLEEDING_CATS)

    class Meta:
        model = Dengue
        fields = "__all__"


class DiagnosisSerializers(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)
    patient_id = serializers.IntegerField(write_only=True)
    patient_name = serializers.StringRelatedField(source='patient', read_only=True)

    class Meta:
        model = Diagnosis
        fields = "__all__"
