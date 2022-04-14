from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from dashboard.healthCareWorkers.api.urls import router as hcwRouter
from dashboard.patients.api.urls import router as patientRouter
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi






#router setup
router = DefaultRouter()
router.registry.extend(patientRouter.registry)
router.registry.extend(hcwRouter.registry)
# API Documentation with swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Dengue Dashboard API",
      default_version='v1',
      description="Documentation of the Dengue Dashboard API",
      terms_of_service="",
      contact=openapi.Contact(email="code@nordglueck.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
                  path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
                  path(
                      "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
                  ),
                  # Django Admin, use {% url 'admin:index' %}
                  path(settings.ADMIN_URL, admin.site.urls),
                  # User management
                  path("users/", include("dashboard.users.urls", namespace="users")),
                  # path("accounts/", include("allauth.urls")),
                  # Your stuff: custom urls includes go here
                  path("api-auth/", include("rest_framework.urls")),
                  path("api/rest-auth/", include("rest_auth.urls")),
                  path("api/rest-auth/login/", include("rest_auth.urls")),
                  path("api/rest-auth/logout/", include("rest_auth.urls")),
                  path("api/", include(router.urls)),
                  path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
urlpatterns += [
    # API base url
    # path("api/", include("config.api_router")),
    path("api/", include(router.urls)),
    # DRF auth token
    #path("auth-token/", obtain_auth_token),
    # path("api-auth/", include("rest_framework.urls")),
    # path("api/rest-auth/", include("rest_auth.urls")),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
