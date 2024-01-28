from django.urls import path
from components.notifications import streaming_view

urlpatterns = [
    path(
        "notification/",
        streaming_view,
        name="stream_notification",
    ),
]
