# [OWN_DD]
# Authors: Jennifer Horstmann, alma@uni-bremen.de

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from dashboard.patients.api.views import ReportViewSet, PatientViewSet, ReportHistoryViewSet, DengueViewSet, \
    DiagnosisViewSet

router = DefaultRouter()
router.register(r"patients", PatientViewSet, basename="patients")
router.register(r"reports", ReportViewSet, basename="reports")
router.register(r"history", ReportHistoryViewSet, basename="history")
router.register(r"dengue", DengueViewSet, basename="dengue")
router.register(r"diagnosis", DiagnosisViewSet, basename="diagnosis")

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns += [
    path('token-auth/', obtain_auth_token, name='api-tokn-auth')
]
