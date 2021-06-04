from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from blog.models import BlogPost

@admin.register(BlogPost)
class BlogPost(admin.ModelAdmin):
    list_display = ('title', 'description', 'created', 'post_image')