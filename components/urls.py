from django.urls import path
from components.counter import CounterComponent
from components.stateless_counter import StatelessCounterComponent
from components.notifications import stream_component

urlpatterns = [
    path("counter/<str:method>/<int:id>", CounterComponent.as_view(), name="counter"),
    path(
        "stateless_counter/<str:method>/<int:id>",
        StatelessCounterComponent.as_view(),
        name="stateless_counter",
    ),
    path(
        "notification/",
        stream_component,
        name="stream_notification",
    ),
]
