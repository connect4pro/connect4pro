from django.contrib import admin
# from .models import Question, Answer, Result
from .models import Question, Choice, Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'visible', 'max_points')

@admin.register(Choice)
class ChoiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'points', 'lock_other')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'choice', 'created')

# @admin.register(Question)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'max_points',)

# @admin.register(Answer)
# class AnswersAdmin(admin.ModelAdmin):
#     list_display = ('answers',)


# @admin.register(Result)
# class ResultAdmin(admin.ModelAdmin):
#     list_display = ("user", 'question', "user_answer",)