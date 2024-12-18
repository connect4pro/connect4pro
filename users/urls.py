from django.urls import path
from users.views import BusinessUserList, BusinessUserRegister, ProviderUserList, ProviderUserRegister, \
    BusinessProfileDetail, ProviderProfileDetail, ProviderUserUpdate, BusinessUserUpdate, SkillList, KnowledgeList, \
    MethodList

from users.views import SectorList

app_name = 'users'

urlpatterns = [
    path('api/users/business', BusinessUserList.as_view(), name='business'),
    path('api/users/provider', ProviderUserList.as_view(), name='providers'),
    path('api/users/register/business', BusinessUserRegister.as_view(), name='business_register'),
    path('api/users/register/provider', ProviderUserRegister.as_view(), name='provider_register'),
    path('api/users/business/detail/<id>', BusinessProfileDetail.as_view(), name='business_profile_detail'),
    path('api/users/provider/detail/<id>', ProviderProfileDetail.as_view(), name='provider_profile_detail'),
    path('api/users/business/update/<id>', BusinessUserUpdate.as_view(), name='business_profile_update'),
    path('api/users/provider/update/<id>', ProviderUserUpdate.as_view(), name='provider_profile_update'),
    path('api/sector', SectorList.as_view(), name='sector_list'),
    path('api/skill', SkillList.as_view(), name='skill_list'),
    path('api/knowledge', KnowledgeList.as_view(), name='knowledge_list'),
    path('api/method', MethodList.as_view(), name='method_list'),
]
