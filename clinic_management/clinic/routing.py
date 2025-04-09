from django.urls import path
from clinic.consumers import VideoCallConsumer

websocket_urlpatterns = [
    path("ws/video_call/", VideoCallConsumer.as_asgi()),
]
