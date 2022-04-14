"""
ASGI config for vue-django-cookie project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/

"""
import os
import sys
from pathlib import Path

from django.core.asgi import get_asgi_application

# This allows easy placement of apps within the interior
# dengue_dashboard directory.

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(ROOT_DIR / "dengue_dashboard"))

# If DJANGO_SETTINGS_MODULE is unset, default to the local settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

# This application object is used by any ASGI server configured to use this file.
django_application = get_asgi_application()

# [OWN_DD]
# Authors: Jennifer Horstmann, alma@uni-bremen.de

from channels.auth import AuthMiddlewareStack
from channels.layers import get_channel_layer
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import re_path

from dashboard.patients.consumers import PatientConsumer, ReportConsumer, HistoryConsumer, DengueConsumer, \
    DiagnosisConsumer
from channelsmultiplexer import AsyncJsonWebsocketDemultiplexer
from config.middleware import TokenAuthMiddlewareStack

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": TokenAuthMiddlewareStack(
        URLRouter(
            [re_path(r"^ws/$", AsyncJsonWebsocketDemultiplexer(
                patients=PatientConsumer().as_asgi(),
                reports=ReportConsumer().as_asgi(),
                history=HistoryConsumer().as_asgi(),
                dengue=DengueConsumer().as_asgi(),
                diagnosis=DiagnosisConsumer().as_asgi()
            ).as_asgi()), ]
        )
    ),
})
