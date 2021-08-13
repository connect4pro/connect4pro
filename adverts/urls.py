from django import urls
from django.urls import path
from adverts.views import CategoryList, BusinessAdvertList, ProviderAdvertList, BusinessAdvertUpdate, \
    ProviderAdvertUpdate, BusinessAdvertDetail, ProviderAdvertDetail, BusinessAdvertCommentCreate, \
    ProviderAdvertCommentCreate, BusinessAdvertCommentList, ProviderAdvertCommentList

urlpatterns = [
    path('api/categories', CategoryList.as_view(), name='category-list'),
    path('api/businessadverts', BusinessAdvertList.as_view(), name='businessadverts'),
    path('api/provideradverts', ProviderAdvertList.as_view(), name='provideradverts'),
    path('api/businessadverts/update/<id>', BusinessAdvertUpdate
         .as_view(), name='businessadverts_update'),
    path('api/provideradverts/update/<id>', ProviderAdvertUpdate
         .as_view(), name='provideradverts_update'),
    path('api/businessadverts/detail/<id>', BusinessAdvertDetail.as_view(), name='businessadverts_detail'),
    path('api/provideradverts/detail/<id>', ProviderAdvertDetail.as_view(), name='provideradverts_detail'),
    path('api/businessadverts/comments/create_comment', BusinessAdvertCommentCreate.as_view(),
         name='businessadvert_comment_create'),
    path('api/provideradverts/comments/create_comment', ProviderAdvertCommentCreate.as_view(),
         name='provideradverts_comment_create'),
    path('api/businessadverts/comments', BusinessAdvertCommentList.as_view(), name='businessadverts_comments_list'),
    path('api/provideradverts/comments', ProviderAdvertCommentList.as_view(), name='provideradverts_comments_list'),

]
