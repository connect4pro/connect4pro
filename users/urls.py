from django.urls import path
from django.views.decorators.http import require_POST

from users.views import BusinessUserList, BusinessUserRegister, ProviderUserRegister

app_name = 'users'

urlpatterns = [
    path('api/users/', BusinessUserList.as_view(), name='users'),
    path('api/users/register/business', BusinessUserRegister.as_view(), name='business_register'),
    path('api/users/register/provider', ProviderUserRegister.as_view(), name='provider_register'),
]