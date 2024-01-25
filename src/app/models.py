from django.db import models


class Counter(models.Model):
    count = models.IntegerField(default=0)


class Notification(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
