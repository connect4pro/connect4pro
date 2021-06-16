from django.contrib import admin
from .models import *

class ChoiceInlineModel(admin.TabularInline):
    model = Choice
    fields = ['possible_answer']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInlineModel]
    list_display = ['id', 'title']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'final_answer']

@admin.register(ResultPoll)
class ResultPollAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'questions', 'answers', 'avg_points']