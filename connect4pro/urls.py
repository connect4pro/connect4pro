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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from adverts.views import CategoryList, BusinessAdvertList, ProviderAdvertList, BusinessAdvertUpdate, \
    ProviderAdvertUpdate
from blog.views import BlogPostList

from rest_framework.urlpatterns import format_suffix_patterns
from events.views import EventList, EventCreate
from faq.views import QuestionsAndAnswersList, QuestionsAndAnswersCreate, WriteUsList, WriteUsCreate
from grants_and_investments.views import GrantList, GrantCreate, InvestmentList, InvestmentCreate
from users.views import facebook_auth

from .yasg import urlpatterns as yasg_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categories', CategoryList.as_view(), name='category-list'),
    path('api/businessadverts', BusinessAdvertList.as_view(), name='businessadverts'),
    path('api/businessadverts/update/<id>', BusinessAdvertUpdate
         .as_view(), name='businessadverts_update'),
    path('api/provideradverts/update/<id>', ProviderAdvertUpdate
         .as_view(), name='provideradverts_update'),
    path('api/provideradverts', ProviderAdvertList.as_view(), name='provideradverts'),
    path('api/blogposts', BlogPostList.as_view()),
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

    path('', include('users.urls')),
    path('api/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('auth/facebook', facebook_auth)

]

urlpatterns += yasg_urls
