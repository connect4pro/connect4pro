from django.contrib import admin

# Register your models here.
from adverts.models import BusinessAdvert, Category, ProviderAdvert

admin.site.register(Category)
admin.site.register(BusinessAdvert)
admin.site.register(ProviderAdvert)
