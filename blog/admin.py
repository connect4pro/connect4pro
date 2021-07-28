from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from blog.models import BlogPost, BlogComment


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created', 'post_image')


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'post')
