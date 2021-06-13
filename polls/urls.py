from django.urls import path
from .views import GetQuestion, QuestionAnswer

app_name = 'polls'

urlpatterns = [
    path('api/polls/get_question', GetQuestion.as_view()),
    path('api/polls/answer', QuestionAnswer.as_view()),
]