from django.contrib import admin

# Register your models here.
from users.models import Connect4ProUser


@admin.register(Connect4ProUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['email']