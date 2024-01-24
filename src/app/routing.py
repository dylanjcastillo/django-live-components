# routing.py
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app import consumers

websocket_urlpatterns = [
    path("feed", consumers.TweetConsumer.as_asgi()),
]

application = ProtocolTypeRouter(
    {
        "websocket": URLRouter(websocket_urlpatterns),
    }
)
