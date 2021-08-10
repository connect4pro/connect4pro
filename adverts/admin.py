from django.contrib import admin
from adverts.models import BusinessAdvert, Category, ProviderAdvert, BusinessAdvertComment, ProviderAdvertComment, \
    Album, Image

admin.site.register(Category)


@admin.register(BusinessAdvert)
class BusinessAdvertAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'price', 'currency', 'category', 'completed']
    list_filter = ['currency', 'category__name', 'completed']


@admin.register(ProviderAdvert)
class ProviderAdvertAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'price', 'currency', 'category']
    list_filter = ['currency', 'category__name']


@admin.register(BusinessAdvertComment)
class BusinessAdvertCommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'post')


@admin.register(ProviderAdvertComment)
class ProviderAdvertCommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'post')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'album')