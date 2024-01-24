from app import views

from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("post_tweet/", views.post_tweet, name="post_tweet"),
    path("register/", views.register, name="register"),
]
