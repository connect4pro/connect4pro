from django.urls import path
from .views import *

app_name = 'polls'

urlpatterns = [
    path('api/poll/question_list', QuestionList.as_view()),
    path('api/poll/question_create', QuestionCreate.as_view()),

    path('api/poll/choice_list', ChoiceList.as_view()),
    path('api/poll/choice_create', ChoiceCreate.as_view()),

    path('api/poll/answer_list', AnswerList.as_view()),
    path('api/poll/answer_create', AnswerCreate.as_view()),

    path('api/poll/pollresult_list', PollResultList.as_view()),
    path('api/poll/pollresult_create', PollResultCreate.as_view()),
]