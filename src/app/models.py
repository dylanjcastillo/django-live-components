# models.py
from django.contrib.auth.models import User
from django.db import models


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    retweets = models.IntegerField(default=0)
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
