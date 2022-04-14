# [OWN_DD]
# Author: alma@uni-bremen.de
from multiselectfield import MultiSelectField

from dashboard.users.models import User
from django.db import models
from dashboard.patients.models import Patient
from django.contrib.postgres.fields import ArrayField, JSONField


class HealthCareDepartment(models.Model):
    name = models.CharField(max_length=240)
    contact_email = models.EmailField(max_length=240, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    changed_by = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class HealthCareWorker(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40, null=True, blank=True)
    healthCareDepartment = models.ForeignKey(HealthCareDepartment, on_delete=models.CASCADE,
                                             related_name="healthcareWorkers", null=True, )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    changed_by = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName


class Case(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="cases")
    healthcareWorker = models.ForeignKey(HealthCareWorker, on_delete=models.CASCADE, null=True)
    # disease_type = models.CharField(blank=True, null=True, max_length=100, verbose_name="disease_type",
    #                                 choices=[
    #                                     ('Dengue', 'Dengue'), ('Others', 'Others')])

    # disease_status = models.CharField(blank=True, null=True, max_length=100, verbose_name="disease_status",
    #                                   choices=[
    #                                       ('Confirmed', 'Confirmed'), ('Suspicious', 'Suspicious'),
    #                                       ('Covered', 'Covered')])
    note = models.CharField(blank=True, null=True, max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    changed_by = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE)

    class Meta:
        get_latest_by = "updated_at"
        ordering = ["updated_at"]

    def __str__(self):
        return str(self.id)


# class Notification(models.Model):
#     case = models.ForeignKey(Case, on_delete=models.CASCADE)
#     healthCareDepartment = models.ForeignKey(HealthCareDepartment, null=True, on_delete=models.CASCADE)
#     note = models.CharField(max_length=2000, null=True, blank=True)
#     notificationDate = models.DateTimeField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     changed_by = models.ForeignKey(
#         User, null=True, on_delete=models.CASCADE)
#
#     class Meta:
#         get_latest_by = "updated_at"
#         ordering = ["updated_at"]
#
#     def __str__(self):
#         return str(self.id)

ADDRESS_CAT = [("home", "home"), ("school", "school"), ("work", "work"), ("others", "others"), (None, "null")]


class Address(models.Model):
    """
    Patient locations.
    """
    cases = models.ForeignKey(Case, on_delete=models.CASCADE, related_name="Addresses", blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="Addresses")
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="Addresses", blank=True, null=True)
    physicalAddress = models.CharField(blank=True, null=True, max_length=1000)
    note = models.CharField(max_length=1000, blank=True, null=True, )
    descriptions = models.CharField(max_length=10000, blank=True, null=True, )
    longitude = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=17, verbose_name="longitude")
    latitude = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=17, verbose_name="latitude")
    arrivalDate = models.DateTimeField(blank=True, null=True)
    departureDate = models.DateTimeField(blank=True, null=True)
    cleanedDate = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=240, blank=True, null=True, choices=ADDRESS_CAT,
                                default="home")  # MultiSelectField(choices=ADDRESS_CAT,null=True,blank=True,default=None)
    addressStatus = models.CharField(max_length=20, default='notStarted',
                                     choices=[('notStarted', 'not started'), ('in progress', 'inProgress'),
                                              ('cleaned', 'cleaned')])
    tasks = JSONField(null=True)
    assigneeID = models.CharField(max_length=240, blank=True, null=True, )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = "updated_at"
        ordering = ["updated_at"]

    def __str__(self):
        return self.cases
