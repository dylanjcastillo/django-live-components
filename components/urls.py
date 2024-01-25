from django.urls import path
from components.counter import CounterComponent

urlpatterns = [
    path("counter/<str:method>/<int:id>", CounterComponent.as_view(), name="counter"),
]
