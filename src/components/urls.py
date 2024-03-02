from django.urls import path
from components.notification import NotificationComponent

urlpatterns = [
    path(
        "notification/",
        NotificationComponent.as_live_view(),
        name="stream_notification",
    ),
]
