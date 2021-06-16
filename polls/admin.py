from django.contrib import admin
from .models import *

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'final_answer', 'poll_result']


class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(ResultPoll)
class ResultPollAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['id', 'user', 'avg_points']