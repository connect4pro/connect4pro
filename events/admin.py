from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from events.models import Event, EventComment
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'location', 'event_format', 'sum', 'event_image')

@admin.register(EventComment)
class EventCommentAdmin(admin.ModelAdmin):
    list_display = ('commentator_text', 'commentator_name', 'commentator_email', 'event')