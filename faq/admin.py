from django.contrib import admin
from faq.forms import PostModelForm
from faq.models import WriteUs, QuestionsAndAnswers


@admin.register(WriteUs)
class WriteUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'message')


@admin.register(QuestionsAndAnswers)
class QuestionsAndAnswersAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    form = PostModelForm
