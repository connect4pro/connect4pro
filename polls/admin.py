from django.contrib import admin
from .models import Choices, GetPoll, Question

@admin.register(Question)
class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'question',)

@admin.register(Choices)
class GetResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'option_count',)

@admin.register(GetPoll)
class GetPollAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'choose_option',)
