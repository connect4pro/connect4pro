from django import urls
from django.urls import path
from adverts.views import CategoryList, BusinessAdvertList, ProviderAdvertList, BusinessAdvertUpdate, ProviderAdvertUpdate

urlpatterns = [
    path('api/categories', CategoryList.as_view(), name='category-list'),
    path('api/businessadverts', BusinessAdvertList.as_view(), name='businessadverts'),
    path('api/businessadverts/update/<id>', BusinessAdvertUpdate
         .as_view(), name='businessadverts_update'),
    path('api/provideradverts/update/<id>', ProviderAdvertUpdate
         .as_view(), name='provideradverts_update'),
    path('api/provideradverts', ProviderAdvertList.as_view(), name='provideradverts'),
]