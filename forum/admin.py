from django.contrib import admin
from .models import Author, Category, Comment, Reply, Post
# Register your models here.

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Post)