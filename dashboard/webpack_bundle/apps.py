from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WebpackBundleConfig(AppConfig):
    name = "dashboard.webpack_bundle"
    verbose_name = _("Webpack Bundle")
