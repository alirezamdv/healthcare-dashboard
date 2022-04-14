# [OWN_DD]
# Authors: Jennifer Horstmann, alma@uni-bremen.de

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from dashboard.healthCareWorkers.api.views import HealthCareWorkerViewSet, HealthCareDepartmentViewSet, CaseViewSet, \
    AddressViewSet

router = DefaultRouter()
router.register(r"healthcareworker", HealthCareWorkerViewSet, basename="healthcareworker")
router.register(r"healthcaredepartment", HealthCareDepartmentViewSet, basename="healthcaredepartment")
router.register(r"case", CaseViewSet, basename="case")
router.register(r"addresses", AddressViewSet, basename="addresses")
# router.register(r"notification", NotificationsViewSet, basename="notifications")

urlpatterns = [
    path("", include(router.urls)),
]
