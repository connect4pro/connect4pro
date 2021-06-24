from django.urls import path
from grants_and_investments.views import GrantList, GrantCreate, InvestmentList, InvestmentCreate, GrantInvestmentCommentList, GrantInvestmentCommentCreate

app_name = 'grants_and_investments'

urlpatterns = [
    path('api/grants', GrantList.as_view(), name = 'grants'),
    path('api/grants/create_grant', GrantCreate.as_view(), name = 'create_grant'),
    path('api/investments', InvestmentList.as_view(), name = 'investments'),
    path('api/investments/create_investment', InvestmentCreate.as_view(), name = 'create_investment'),
    path('api/grants_and_investments/comments', GrantInvestmentCommentList.as_view(), name = 'grants_and_investments_comments'),
    path('api/grants_and_investments/comments/create_comment', GrantInvestmentCommentCreate.as_view(), name = 'grants_and_investments_comments_create'),
]