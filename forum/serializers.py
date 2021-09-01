from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from forum.models import Author, Category, Post, Comment


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'fullname', 'bio']
        read_only_fields = ('slug',)


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required = False)
    title = serializers.CharField(required = True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']
        read_only_fields = ('slug',)


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required = False)
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content', 'category']
        read_only_fields = ('slug',)

    def create(self, validated_data):
        category = dict(validated_data.pop('category'))['id']
        category = Category.objects.get(id = category)
        new_post = Post.objects.create(category = category, user = validated_data['user'], title = validated_data['title'], content = validated_data['content'])
        new_post.save()
        return new_post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id',)