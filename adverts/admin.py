from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from adverts.models import BusinessAdvert, Category, ProviderAdvert


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(BusinessAdvert)
class BusinessAdvertAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description', 'price', 'currency', 'completed', 'user')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('user').all()
        return queryset


@admin.register(ProviderAdvert)
class ProviderAdvertAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_1', 'image_2', 'category', 'price', 'currency', 'user')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('category').all()
        return queryset