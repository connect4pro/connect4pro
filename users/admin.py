from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Connect4ProUser, BusinessProfile, ProviderProfile, Sector, Skill, Method, Knowledge


@admin.register(Connect4ProUser)
class Connect4ProUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'is_premium', 'is_business', 'is_provider']
    list_filter = ['is_premium', 'is_business', 'is_provider']


@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'turnover', 'employers']
    list_filter = ['employers', 'turnover', 'sector']


@admin.register(ProviderProfile)
class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Method)
class MethodAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Knowledge)
class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.site_title = 'Connect4pro'  # тайтл как <titlle></title>
admin.site.site_header = 'Connect4pro'  # тайтл вверху админки
admin.site.register(UserAdmin)