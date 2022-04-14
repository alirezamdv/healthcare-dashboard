# [OWN_DD]
# Author: Jennifer Horstmann

from django.contrib import admin
from .models import HealthCareWorker,HealthCareDepartment

admin.site.register(HealthCareWorker)
admin.site.register(HealthCareDepartment)
