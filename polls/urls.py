from django.urls import path
from .views import *

app_name = 'polls'

urlpatterns = [
    path('api/poll/question_list', QuestionList.as_view()),

    path('api/poll/answer_list', AnswerList.as_view()),
    # path('api/poll/answer_create', AnswerCreate.as_view()),

    path('api/poll', PollResultId.as_view()),
    path('api/poll/<int:poll_id>/<int:question_id>', AnswerCreate.as_view()),
]