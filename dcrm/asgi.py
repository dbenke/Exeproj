import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
import dcrm.routing
from channels.auth import AuthMiddlewareStack


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcrm.settings')

application = ProtocolTypeRouter(
   {
      'http':get_asgi_application(),
      #'websocket': URLRouter(dcrm.routing.websocket_urlpatterns),
      'websocket': AuthMiddlewareStack(
         URLRouter(
            dcrm.routing.websocket_urlpatterns
         )
      ),

   }
) 