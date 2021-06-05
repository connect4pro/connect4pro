from django.urls import path
from blog.views import BlogPostList

urlpatterns = [
    path('api/blogposts', BlogPostList.as_view()),
]