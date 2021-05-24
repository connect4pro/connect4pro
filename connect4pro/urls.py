"""connect4pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from adverts.views import CategoryList, CategoryCreate, UserAdvertList, UserAdvertCreate
from events.views import EventList, EventCreate
from faq.views import QuestionsAndAnswersList, QuestionsAndAnswersCreate, WriteUsList, WriteUsCreate
from grants_and_investments.views import GrantList, GrantCreate, InvestmentList, InvestmentCreate
from .yasg import urlpatterns as yasg_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categories', CategoryList.as_view()),
    path('api/categories/create_category', CategoryCreate.as_view()),
    path('api/useradverts', UserAdvertList.as_view()),
    path('api/useradverts/create_advert', UserAdvertCreate.as_view()),
    path('api/events', EventList.as_view(), name = 'events'),
    path('api/events/create', EventCreate.as_view(), name = 'event-create'),
    path('api/questions_and_answers', QuestionsAndAnswersList.as_view(), name = 'questions_and_answers'),
    path('api/questions_and_answers/create', QuestionsAndAnswersCreate.as_view(),name = 'questions_and_answers-create'),
    path('api/write_us', WriteUsList.as_view(), name = 'write_us'),
    path('api/write_us/create_message', WriteUsCreate.as_view(), name = 'create-message'),
    path('api/grants', GrantList.as_view(), name = 'grants'),
    path('api/grants/create_grant', GrantCreate.as_view(), name = 'create-grant'),
    path('api/investments', InvestmentList.as_view(), name = 'investments'),
    path('api/investments/create_investment', InvestmentCreate.as_view(), name = 'create-investment'),
    path('api-auth/', include('rest_framework.urls')),
]
# urlpatterns += router.urls
# urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += yasg_urls