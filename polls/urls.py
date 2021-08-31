from django.urls import path
from .views import *

app_name = 'polls'

urlpatterns = [
    path('api/poll/question_list', QuestionList.as_view()),

    path('api/poll/answer_list', AnswerList.as_view()),
    # path('api/poll/answer_create', AnswerCreate.as_view()),

    path('api/poll', PollResultId.as_view()),
    path('api/poll/<int:poll_id>/<int:question_id>', AnswerCreate.as_view()),
<<<<<<< HEAD
    path('api/poll/send_result', send_result, name='send_result'),
=======
>>>>>>> 803b5d8895726f93043b67deacb9a6807f91452f
    path('api/poll/send_form', ConsultationFormSend.as_view()),
]