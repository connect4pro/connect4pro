from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from forum.models import Author, Category, Post, Reply, Comment


class AuthorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    # user = serializers.SerializerMethodField(source='get_user')
    class Meta:
        model = Author
        fields = ('user','fullname', 'bio')
        read_only_fields = ('id', 'slug')

    # def get_user(self, obj):
    #     return obj.user.username

class CategorySerializer(serializers.ModelSerializer):
    title = serializers.StringRelatedField()
    class Meta:
        model = Category
        fields = ('title', 'slug', 'description')
        read_only_fields = ('id', 'slug')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Reply
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'