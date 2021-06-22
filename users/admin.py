from django.contrib import admin
from users.models import Connect4ProUser, BusinessProfile, ProviderProfile, Sector


@admin.register(Connect4ProUser)
class Connect4ProUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'is_premium', ]
    list_filter = ['is_premium', 'business_profile__as_business', 'provider_profile__as_provider']


@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'region', 'turnover', 'employers']
    list_filter = ['region', 'turnover']


@admin.register(ProviderProfile)
class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'manager', 'address']


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ['description']


admin.site.site_title = 'Connect4pro'  # тайтл как <titlle></title>
admin.site.site_header = 'Connect4pro'  # тайтл вверху админки
