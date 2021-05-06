from django.contrib import admin

# Register your models here.
from adverts.models import UserAdvert, Category

admin.site.register(Category)
admin.site.register(UserAdvert)