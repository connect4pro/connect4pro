from django.urls import path
from .views import QuestionList, ChoicesList, GetPollList

app_name = 'polls'

urlpatterns = [
    path('api/poll/questions_list', QuestionList.as_view()),
    path('api/poll/choices_list', ChoicesList.as_view()),
    path('api/poll/get_poll_list', GetPollList.as_view()),
]