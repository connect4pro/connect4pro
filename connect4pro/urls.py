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
from faq.models import WriteUs
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from adverts.views import CategoryList, UserAdvertList
from events.views import EventList
from faq.views import QuestionsAndAnswersList, WriteUsList
from .yasg import urlpatterns as yasg_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categories', CategoryList.as_view()),
    path('api/useradverts', UserAdvertList.as_view()),
    path('api/events', EventList.as_view()),
    path('api/questions_and_answers', QuestionsAndAnswersList.as_view()),
    path('api/write_us', WriteUsList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
# urlpatterns += router.urls
# urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += yasg_urls