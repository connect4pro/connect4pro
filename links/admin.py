from django.contrib import admin

from links.models import TelegramLinks, TelegramCategory


class LinksInline(admin.TabularInline):
    model = TelegramLinks
    fields = ('ru_link', 'kg_link')


@admin.register(TelegramCategory)
class TelegramCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'link_category')
    inlines = (LinksInline,)

