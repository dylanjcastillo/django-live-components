from app import views

from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("components/", views.stream_components, name="post_tweet"),
]
