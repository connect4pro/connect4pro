from django.contrib import admin
from grants_and_investments.models import Grant, Investment, GrantInvestmentComment


admin.site.register(Grant)
admin.site.register(Investment)
admin.site.register(GrantInvestmentComment)