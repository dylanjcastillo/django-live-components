from django.contrib import admin

# Register your models here.

from app.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("message", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("message",)
