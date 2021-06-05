from django.urls import path
from faq.views import QuestionsAndAnswersList, QuestionsAndAnswersCreate, WriteUsList, WriteUsCreate

app_name = 'faq'

urlpatterns = [
    path('api/questions_and_answers', QuestionsAndAnswersList.as_view(), name = 'questions_and_answers'),
    path('api/questions_and_answers/create', QuestionsAndAnswersCreate.as_view(),name = 'questions_and_answers_create'),
    path('api/write_us', WriteUsList.as_view(), name = 'write_us'),
    path('api/write_us/create_message', WriteUsCreate.as_view(), name = 'create_message'),
]