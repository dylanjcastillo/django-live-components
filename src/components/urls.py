from django.urls import path
from components.notification import streaming_view

urlpatterns = [
    path(
        "notification/",
        streaming_view,
        name="stream_notification",
    ),
]
