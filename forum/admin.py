from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Author, Category, Comment, Post
# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'fullname', 'bio')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('user').all()
        return queryset


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')


@admin.register(Post)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'content', 'category', 'date')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('category').all()
        return queryset

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'comment', 'parent', 'date')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('parent').all()
        return queryset