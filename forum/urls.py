from django.urls import path
from forum.views import AuthorList, AuthorCreate, CategoryList, CategoryCreate, PostList, PostCreate, CommentList, CommentCreate

app_name = 'forum'

urlpatterns = [
    path('api/forum/authors', AuthorList.as_view(), name = 'forum_author_list'),
    path('api/forum/authors/create_author', AuthorCreate.as_view(), name = 'create_author'),
    path('api/forum/categories', CategoryList.as_view(), name = 'forum_category'),
    path('api/forum/categories/create_category', CategoryCreate.as_view(), name = 'create_category'),
    path('api/forum/comments', CommentList.as_view(), name = 'forum_comments'),
    path('api/forum/comments/create_comment', CommentCreate.as_view(), name = 'create_comments'),
    path('api/forum/posts', PostList.as_view(), name = 'post_list'),
    path('api/forum/posts/create_post', PostCreate.as_view(), name = 'create_post'),
]