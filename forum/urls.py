from django.urls import path
from forum.views import home, detail, posts

urlpatterns = [
    path('home', home, name = 'home'),
    path('detail/<slug>/', detail, name = 'detail'),
    path('posts/<slug>/', posts, name = 'posts'),
]