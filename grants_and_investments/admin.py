from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from grants_and_investments.models import Grant, Investment, GrantInvestmentComment


@admin.register(Grant)
class GrantAdmin(admin.ModelAdmin):
    list_display = ('grant_name', 'grant_sum', 'currency', 'grant_deadline', 'grant_description')


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('invest_name', 'invest_sum', 'currency', 'invest_deadline', 'invest_description')

@admin.register(GrantInvestmentComment)
class GrantInvestmentCommentAdmin(admin.ModelAdmin):
    list_display = ('commentator_text', 'commentator_name', 'commentator_email')