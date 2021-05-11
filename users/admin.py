from django.contrib import admin
from users.models import Connect4ProUser, BusinessProfile, ProviderProfile


@admin.register(Connect4ProUser)
class Connect4ProUserAdmin(admin.ModelAdmin):
    list_display = ['email']


@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ['last_name']


@admin.register(ProviderProfile)
class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = ['manager']
