from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from faq.models import WriteUs, QuestionsAndAnswers
# Register your models here.


@admin.register(WriteUs)
class WriteUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'message')


@admin.register(QuestionsAndAnswers)
class QuestionsAndAnswersAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')