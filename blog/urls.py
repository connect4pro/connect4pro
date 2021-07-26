from django.urls import path
from blog.views import BlogPostList, BlogDetail, BlogCommentsList, BlogCommentCreate

urlpatterns = [
    path('api/blogposts', BlogPostList.as_view()),
    path('api/blogposts/detail/<id>', BlogDetail.as_view(), name='blog_create'),
    path('api/blogposts/comments', BlogCommentsList.as_view(), name='blog_comments'),
    path('api/blogposts/comments/create_comment', BlogCommentCreate.as_view(), name='blog_comments_create'),
]
