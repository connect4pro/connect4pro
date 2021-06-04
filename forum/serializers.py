from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from forum.models import Author, Category, Post, Comment


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['user','fullname', 'bio']
        read_only_fields = ('id', 'slug')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug', 'description']
        read_only_fields = ('id', 'slug')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'title', 'category', 'content']
        read_only_fields = ('id', 'slug')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id',)