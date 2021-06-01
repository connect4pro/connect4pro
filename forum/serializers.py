from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from forum.models import Author, Category, Post, Comment


class AuthorSerializer(serializers.ModelSerializer):
    user = StringRelatedField()

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
    user = StringRelatedField()
    category = StringRelatedField()
    class Meta:
        model = Post
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    user = StringRelatedField()
    post = StringRelatedField()
    parent = StringRelatedField()
    class Meta:
        model = Comment
        fields = '__all__'