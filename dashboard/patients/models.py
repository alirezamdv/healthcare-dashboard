# [OWN_DD]
# Authors: Jennifer Horstmann, alma@uni-bremen.de

from datetime import datetime

from dashboard.users.models import User
from django.db import models
from model_utils.fields import MonitorField
from simple_history.models import HistoricalRecords
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator
from django.utils import timezone
from multiselectfield import MultiSelectField


class Patient(models.Model):
    """
    Patient instance.
    """
    HN_validator = RegexValidator(r'^[H][N]\S{5}[/]\d{2}', 'Only HNxxxxx/YY pattern is allowed.')
    AN_validator = RegexValidator(r'^[A][N]\S{5}[/]\d{2}', 'Only ANxxxxx/YY pattern is allowed.')
    first_name = models.CharField(max_length=240, blank=True, null=True)
    last_name = models.CharField(max_length=240, blank=True, null=True)
    patientId = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=0, unique=True)
    admission_number = ArrayField(models.CharField(max_length=240, blank=True, null=True, validators=[AN_validator]),
                                  null=True)
    hospital_number = models.CharField(max_length=240, blank=True, null=True, validators=[HN_validator])
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(blank=True, null=True, default="", choices=[
        ('Male', 'Male'), ('Female', 'Female'), (None, "null")], max_length=10)
    birth_date = models.DateTimeField(blank=True, null=True)
    admission_date = models.DateTimeField(blank=True, null=True)  # DHF too
    enrollment_date = models.DateTimeField(blank=True, null=True)  # DHF too
    dismissal_date = models.DateTimeField(blank=True, null=True)  # DHF too

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = "updated_at"
        ordering = ["updated_at"]

    def __str__(self):
        date = self.updated_at.strftime("%Y/%m/%d")
        return (str(self.first_name)) + " " + (str(self.last_name))


class Report(models.Model):
    """
    Report instance. The history of the report is to be found in the field "history".
    """
    patient = models.OneToOneField(
        Patient, on_delete=models.CASCADE, related_name="reports")
    daytime = models.CharField(max_length=1, blank=False, choices=[
        ('D', 'D'), ('E', 'E'), ('N', 'N')], default='D')  # D, E, N
    datetime = models.DateTimeField(blank=True, null=True, default=datetime.now)
    day_of_fever = models.PositiveIntegerField(blank=True, null=True)
    # fever means temperature # DHF too
    fever = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)
    pulse = models.PositiveIntegerField(blank=True, null=True)
    respiration = models.IntegerField(blank=True, null=True)
    # Blood Pressure # DHF too
    bp_sys = models.PositiveIntegerField(blank=True, null=True)
    bp_dia = models.PositiveIntegerField(blank=True, null=True)
    # Fluid Input # DHF too
    fluid_input = models.PositiveIntegerField(blank=True, null=True)
    fi_oral = models.PositiveIntegerField(blank=True, null=True, verbose_name='oral')
    fi_parenteral = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='parenteral')
    fi_other = models.PositiveIntegerField(blank=True, null=True, verbose_name='other')
    fi_eight_hrs = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='in 8 hours')
    fi_total = models.PositiveIntegerField(blank=True, null=True, verbose_name='total')
    # Fluid Output # DHF too
    fluid_output = models.PositiveIntegerField(blank=True, null=True)
    fo_urine = models.PositiveIntegerField(blank=True, null=True, verbose_name='urine')
    fo_uf = models.PositiveIntegerField(blank=True, null=True, verbose_name='uf')
    fo_emesis = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='emesis')
    fo_drainage = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='drainage')
    fo_eight_hrs = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='in 8 hours')
    fo_total = models.PositiveIntegerField(blank=True, null=True, verbose_name='total')
    # misc
    diet = models.CharField(max_length=1000, blank=True, null=True)
    pain_score = models.PositiveIntegerField(blank=True, null=True)
    abd_cir = models.PositiveIntegerField(blank=True, null=True)
    stools = models.PositiveIntegerField(blank=True, null=True)
    urine = models.PositiveIntegerField(blank=True, null=True)
    # DHF start
    # ---- Admission day -> various parameters can be used in daily reports too. e.g. rash
    # Ever received JE vaccine ?
    je = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="je", choices=[
        ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # Any other febrile illness during the past 2 months?
    febrile = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="febrile",
                               choices=[
                                   ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # First day and time of fever
    fever_date = models.DateTimeField(blank=True, null=True)
    # Headache before enrollment?
    headache = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="headache",
                                choices=[
                                    ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    headache_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='headache_days')
    # How many days?
    myalgia_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='myalgia_days')
    # bone pain before enrollment?
    bone = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="bone", choices=[
        ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    bone_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='bone_days')
    # retro orbital pain before enrollment?
    retro = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="retro", choices=[
        ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    retro_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='retro_days')
    # flushed face before enrollment?
    flushed = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="flushed",
                               choices=[
                                   ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    flushed_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='flushed_days')
    # Rash without itching before enrollment?
    rashwithout = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="rashwithout",
                                   choices=[
                                       ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    rashwithout_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='rashwithout_days')
    # Rash with itching before enrollment?
    rashwith = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="rashwith",
                                choices=[
                                    ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    rashwith_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='rashwith_days')
    # anorexia before enrollment?
    anorexia = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="anorexia",
                                choices=[
                                    ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    anorexia_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='anorexia_days')
    # How many days?
    nausea_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='nausea_days')
    rashwith_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='rashwith_days')
    # vomitting before enrollment?
    vomitting = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="vomitting",
                                 choices=[
                                     ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    vomitting_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='vomitting_days')
    # abdominal pain before enrollment?
    abdominal = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="abdominal",
                                 choices=[
                                     ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    abdominal_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='abdominal_days')
    # drowsiness before enrollment?
    drowsiness = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="drowsiness",
                                  choices=[
                                      ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    drowsiness_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='drowsiness_days')
    # drowsiness before enrollment?
    drowsiness = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="drowsiness",
                                  choices=[
                                      ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    drowsiness_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='drowsiness_days')

    # ---- Bleeding -> only if bleeding yes
    # spontaneous petechiae before enrollment?
    spont = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="spont", choices=[
        ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    spont_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='spont_days')
    # ecchymosis before enrollment?
    ecchy = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="ecchy", choices=[
        ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    ecchy_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='ecchy_days')
    # gum bleeding before enrollment?
    gum = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="gum", choices=[
        ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    gum_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='gum_days')
    # nose bleeding before enrollment?
    nose = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="nose", choices=[
        ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    nose_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='nose_days')
    # vomit bleeding before enrollment?
    vomit_bleeding = models.CharField(blank=True, null=True, default='Unknown', max_length=100,
                                      verbose_name="vomit_bleeding", choices=[
            ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    vomit_bleeding_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='vomit_bleeding_days')
    # stool bleeding before enrollment?
    stool = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="stool", choices=[
        ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    stool_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='stool_days')
    other_bleeding = models.CharField(blank=True, null=True, default='Unknown', max_length=100,
                                      verbose_name="other_bleeding", choices=[
            ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # ---- Bleeding end

    # quantity data of Tourniquet test
    tourniquet_qnt = models.PositiveIntegerField(blank=True, null=True, verbose_name='stool_days')
    # quality data of Tourniquet test
    tourniquet_qlt = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="stool",
                                      choices=[
                                          ('Fine', 'Fine'), ('Medium', 'Medium'), ('Coarse', 'Coarse'),
                                          ('Mixed', 'Mixed'), ('Unknown', 'Unknown')])
    # upper respiratory infection before enrollment?
    uri = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="uri", choices=[
        ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # exudative rhinorrhea before enrollment?
    exud = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="exud", choices=[
        ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    exud_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='exud_days')
    # clear rhinorrhea before enrollment?
    clear = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="clear", choices=[
        ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    clear_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='clear_days')
    # non-productive cough before enrollment?
    non_prod = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="non_prod",
                                choices=[
                                    ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    non_prod_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='non_prod_days')
    # productive cough before enrollment?
    prod = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="prod", choices=[
        ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    prod_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='prod_days')
    # feeling of sore throat before enrollment?
    sore_throat = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="sore_throat",
                                   choices=[
                                       ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    sore_throat_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='sore_throat_days')
    #  diarrhea throat before enrollment?
    diarrhea = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="diarrhea",
                                choices=[
                                    ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    diarrhea_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='diarrhea_days')
    diarrhea = models.CharField(blank=True, null=True, default='Unknown', max_length=100, verbose_name="diarrhea",
                                choices=[
                                    ('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')])
    # How many days?
    diarrhea_days = models.PositiveIntegerField(blank=True, null=True, verbose_name='diarrhea_days')
    # ---- Admission day end
    # Daily parameters / Most are already further on top of this class
    # hct (ward, fingertip, peripheral)
    hct = models.PositiveIntegerField(blank=True, null=True, verbose_name='hct')
    # mental status of patient
    mental_status = models.CharField(blank=True, null=True, max_length=100, verbose_name="mental_status", choices=[
        ('Alert', 'Alert'), ('Drowsy', 'Drowsy'), ('Lethargic', 'Lethargic'), ('Restless', 'Restless'),
        ('Stuporous', 'Stuporous'), ('Comatose', 'Comatose')])
    # confluent petechial
    conflu = models.CharField(blank=True, null=True, max_length=100, verbose_name="conflu", choices=[
        ('Yes', 'Yes'), ('No', 'No')])
    # maculopapular
    maculo = models.CharField(blank=True, null=True, max_length=100, verbose_name="maculo", choices=[
        ('Yes', 'Yes'), ('No', 'No')])
    # convalescent
    conval = models.CharField(blank=True, null=True, max_length=100, verbose_name="conval", choices=[
        ('Yes', 'Yes'), ('No', 'No')])
    # bruising with venipuncture
    bruising = models.CharField(blank=True, null=True, max_length=100, verbose_name="bruising", choices=[
        ('Yes', 'Yes'), ('No', 'No')])
    dyspnea = models.CharField(blank=True, null=True, max_length=100, verbose_name="dyspnea", choices=[
        ('Yes', 'Yes'), ('No', 'No')])
    ascites = models.CharField(blank=True, null=True, max_length=100, verbose_name="ascites", choices=[
        ('Yes', 'Yes'), ('No', 'No')])
    juandice = models.CharField(blank=True, null=True, max_length=100, verbose_name="ascites", choices=[
        ('Yes', 'Yes'), ('No', 'No')])
    # liver tenderness
    liver_tenderness = models.CharField(blank=True, null=True, max_length=100, verbose_name="liver_tenderness",
                                        choices=[
                                            ('Yes', 'Yes'), ('No', 'No')])
    liver_size = models.PositiveIntegerField(blank=True, null=True, verbose_name='liver_size')
    # abdominal circumference
    abdominal_circ = models.PositiveIntegerField(blank=True, null=True, verbose_name='abdominal_circ')
    spleen_size = models.PositiveIntegerField(blank=True, null=True, verbose_name='spleen_size')
    lymph_enlargment = models.CharField(blank=True, null=True, max_length=100, verbose_name="lymph_enlargement",
                                        choices=[
                                            ('Yes', 'Yes'), ('No', 'No')])
    cervical = models.PositiveIntegerField(blank=True, null=True, verbose_name='cervical')
    epitro = models.PositiveIntegerField(blank=True, null=True, verbose_name='epitrochea')
    inginual = models.PositiveIntegerField(blank=True, null=True, verbose_name='inginual')
    # injected conjunctivae
    injected = models.CharField(blank=True, null=True, max_length=100, verbose_name="injected", choices=[
        ('Yes', 'Yes'), ('No', 'No')])
    limbus = models.CharField(blank=True, null=True, max_length=100, verbose_name="limbus", choices=[
        ('Yes', 'Yes'), ('No', 'No')])
    bulbar = models.CharField(blank=True, null=True, max_length=100, verbose_name="bulbar", choices=[
        ('Yes', 'Yes'), ('No', 'No')])
    transfusion = models.PositiveIntegerField(blank=True, null=True, verbose_name='transfusion')
    crystalline = models.PositiveIntegerField(blank=True, null=True, verbose_name='crystalline')
    form1 = models.PositiveIntegerField(blank=True, null=True, verbose_name='form1')
    form2 = models.PositiveIntegerField(blank=True, null=True, verbose_name='form2')
    form3 = models.PositiveIntegerField(blank=True, null=True, verbose_name='form3')
    form4 = models.PositiveIntegerField(blank=True, null=True, verbose_name='form4')
    form4x = models.PositiveIntegerField(blank=True, null=True, verbose_name='form4x')
    dextran = models.PositiveIntegerField(blank=True, null=True, verbose_name='dextran')
    haesteryl = models.PositiveIntegerField(blank=True, null=True, verbose_name='haesteryl')
    hct = models.PositiveIntegerField(blank=True, null=True, verbose_name='hct')
    wbc = models.PositiveIntegerField(blank=True, null=True, verbose_name='wbc')
    pmn = models.PositiveIntegerField(blank=True, null=True, verbose_name='pmn')
    band = models.PositiveIntegerField(blank=True, null=True, verbose_name='band')
    lymp = models.PositiveIntegerField(blank=True, null=True, verbose_name='lymp')
    atyp = models.PositiveIntegerField(blank=True, null=True, verbose_name='atyp')
    mono = models.PositiveIntegerField(blank=True, null=True, verbose_name='mono')
    baso = models.PositiveIntegerField(blank=True, null=True, verbose_name='baso')
    eosin = models.PositiveIntegerField(blank=True, null=True, verbose_name='eosin')
    platelet = models.PositiveIntegerField(blank=True, null=True, verbose_name='platelet')
    lft_protein = models.PositiveIntegerField(blank=True, null=True, verbose_name='lft_protein')
    lft_albumin = models.PositiveIntegerField(blank=True, null=True, verbose_name='lft_albumin')
    lft_ast = models.PositiveIntegerField(blank=True, null=True, verbose_name='lft_ast')
    lft_alt = models.PositiveIntegerField(blank=True, null=True, verbose_name='lft_alt')
    eff_1 = models.PositiveIntegerField(blank=True, null=True, verbose_name='eff_1')
    eff_2 = models.PositiveIntegerField(blank=True, null=True, verbose_name='eff_2')
    eff_amount = models.PositiveIntegerField(blank=True, null=True, verbose_name='eff_amount')
    # DHF end

    weight_ht = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='weight/ht')
    weight = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)  # DHF too
    height = models.PositiveIntegerField(blank=True, null=True, verbose_name='height')  # DHF too
    o2sat = models.PositiveIntegerField(blank=True, null=True, verbose_name="O2 Saturation")
    hematocrit = models.PositiveIntegerField(blank=True, null=True)
    platelet = models.PositiveIntegerField(blank=True, null=True)
    wbc = models.PositiveIntegerField(blank=True, null=True)
    warning_signs = models.CharField(max_length=1000, blank=True, null=True, verbose_name="Warning Signs")
    additional = models.CharField(max_length=1000, blank=True, null=True, verbose_name="Additional Info")
    medical_advice = models.CharField(max_length=1000, blank=True, null=True, verbose_name="Medical Advice")
    status = models.CharField(blank=True, null=True, max_length=20, choices=[
        ('febrile', 'febrile'), ('critical', 'critical'), ('recovery', 'recovery')])
    status_changed_to_critical = MonitorField(
        monitor='status', when=['critical'], editable=False)
    monitoring_interval = models.SmallIntegerField(blank=True, null=True, choices=[
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])
    history = HistoricalRecords(user_model=User, related_name="logs")
    created_at = models.DateTimeField(auto_now_add=True)  # DHF too
    updated_at = models.DateTimeField(auto_now=True)
    changed_by = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE)

    class Meta:
        get_latest_by = "datetime"
        ordering = ["datetime"]

    def __str__(self):
        return "Report of Patient: " + str(self.patient)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class Dengue(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="dengue")
    occ2 = models.CharField(max_length=240, verbose_name="occupation", blank=True, null=True, default="",
                            choices=[('Employee', 'Employee'), ('Officer', 'Officer'), ("Student", "Student"),
                                     ("Other", "Other"), (None, "null")])
    age = models.IntegerField(blank=True, null=True)
    bleeding = models.CharField(blank=True, null=True, max_length=10, default="", choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])  # DHF too

    # Bleeding category start
    gum_bleeding = models.CharField(blank=True, null=True, max_length=10, default="", choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])
    gastrointestinal_bleeding = models.CharField(blank=True, null=True, max_length=10, default="", choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])
    epistaxis = models.CharField(blank=True, null=True, max_length=10, default="", choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])
    other_mucosal_bleeding = models.CharField(blank=True, null=True, default="", max_length=10, choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])
    menstrual_bleeding = models.CharField(blank=True, null=True, default="", max_length=10, choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])
    other_bleeding = models.CharField(blank=True, null=True, max_length=10, default="", choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])

    # Bleeding category end

    incidencerate = models.CharField(blank=True, null=True, max_length=100, default="", verbose_name="incidence_rate",
                                     choices=[
                                         ('incidencerate1', 'incidencerate1'), ('incidencerate2', 'incidencerate2'),
                                         (None, "null")])
    UD2 = models.CharField(blank=True, null=True, max_length=100, verbose_name="UD2", default="", choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])
    NS1 = models.CharField(blank=True, null=True, max_length=100, verbose_name="NS1", default="", choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])
    wbc_d0 = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=4)
    plt = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=4)
    lymp_d0 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=4)
    hct_d0 = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=4)
    atypl_d0 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=4)
    ast = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=4)
    alt = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=4)
    tourniquettest = models.CharField(blank=True, null=True, max_length=10, default="", choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])
    nausea = models.CharField(blank=True, null=True, max_length=10, default="", choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])
    petechiae = models.CharField(blank=True, null=True, max_length=10, default="", choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])
    myalgia = models.CharField(blank=True, null=True, max_length=10, default="", choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])
    userID = models.IntegerField(blank=True, null=True)
    eschar = models.CharField(blank=True, null=True, max_length=10, default="", choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])
    hasFever = models.CharField(blank=True, null=True, max_length=10, default="", choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])
    calfPain = models.CharField(blank=True, null=True, max_length=10, default="", choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])
    abdominalPain = models.CharField(blank=True, null=True, max_length=10, default="", choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])
    feverdays = models.IntegerField(blank=True, null=True)
    outcome_bn = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=7)
    lastCalculated = models.DateTimeField(blank=True, null=True)
    sensitivityAnalysis = models.CharField(blank=True, null=True, max_length=1000, default="")
    outcomeRl = models.CharField(blank=True, null=True, max_length=10, default="", choices=[
        ('Positive', 'Positive'), ('Negative', 'Negative'), (None, "null")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lastEditor = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "report of dengue parameter of patient: " + str(self.patient)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class Diagnosis(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="diagnosis")
    disease_type = models.CharField(blank=True, null=True, max_length=100, verbose_name="diagnosis", choices=[
        ('Dengue', 'Dengue'), ('DHF', 'DHF'), ('Influenza', 'Influenza'), ('Others', 'Others')])
    status = models.CharField(blank=True, null=True, max_length=100, verbose_name="status", choices=[
        ('Confirmed', 'Confirmed'), ('Suspected', 'Suspected'), ('Negative', 'Negative')])
    note = models.CharField(max_length=2000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    changed_by = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "Diagnosis of patient: " + str(self.patient)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
