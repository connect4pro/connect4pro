from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from forum.models import Author, Category, Post, Comment


class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required = False)
    email = serializers.CharField(required = True)

    class Meta:
        model = Author
        fields = ['id', 'email', 'fullname', 'bio']
        read_only_fields = ('slug',)


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required = False)

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'description']
        read_only_fields = ('slug',)


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required = False)
    category = CategorySerializer()
    user = AuthorSerializer()

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content', 'category']
        read_only_fields = ('slug',)

    def create(self, validated_data):
        category = dict(validated_data.pop('category'))['id']
        category = Category.objects.get(id = category)
        post = Post.objects.create(category = category, user = validated_data['user'], title = validated_data['title'], content = validated_data['content'])
        post.save()
        return post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id',)
