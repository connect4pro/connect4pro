from django.urls import path

from grants_and_investments.views import GrantsList, GrantDetail, GrantCommentCreate, GrantCommentList
# InvestList, InvestDetail, InvestCommentList, InvestmentCommentCreate

app_name = 'grants_and_investments'

urlpatterns = [
    path('api/grants', GrantsList.as_view()),
    path('api/grants/detail/<id>', GrantDetail.as_view(), name='grant_create'),
    path('api/grants/comments', GrantCommentList.as_view(), name='grant_comments'),
    path('api/grants/comments/create_comment', GrantCommentCreate.as_view(), name='grant_comments_create'),
    # path('api/invests', InvestList.as_view()),
    # path('api/invests/detail/<id>', InvestDetail.as_view(), name='invest_create'),
    # path('api/invests/comments', InvestCommentList.as_view(), name='invest_comments'),
    # path('api/invests/comments/create_comment', InvestmentCommentCreate.as_view(), name='invest_comments_create'),
]
