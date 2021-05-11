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
from adverts.views import CategoryList, BusinessAdvertList
from blog.views import BlogPostList
from .yasg import urlpatterns as yasg_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categories', CategoryList.as_view(), name='category-list'),
    path('api/useradverts', BusinessAdvertList.as_view(), name='useradverts'),
    path('api/blogposts', BlogPostList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += yasg_urls