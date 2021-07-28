from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from grants_and_investments.models import Grant, Investment, GrantComment, InvestmentComment


@admin.register(Grant)
class GrantAdmin(admin.ModelAdmin):
    list_display = ('name', 'sum', 'currency', 'deadline', 'description')


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'sum', 'currency', 'deadline', 'description')

@admin.register(GrantComment)
class GrantCommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user',  'post')


@admin.register(InvestmentComment)
class InvestmentCommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user',  'post')
