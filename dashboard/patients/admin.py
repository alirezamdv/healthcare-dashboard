# [OWN_DD]
# Author: Jennifer Horstmann

from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Patient, Report

admin.site.register(Patient)
admin.site.register(Report, SimpleHistoryAdmin)
