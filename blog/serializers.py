from rest_framework import serializers

from adverts.serializers import UserSerializer
from blog.models import BlogPost, BlogComment


class BlogCommentSerializer(serializers.ModelSerializer):
    """Blog comment serialize"""
    user = UserSerializer()

    class Meta:
        model = BlogComment
        fields = ['id', 'post', 'text', 'user', 'posted']


class BlogPostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    comments = BlogCommentSerializer(source='post_comment', many=True)
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'subtitle', 'description', 'created', 'post_image', 'comments']
        depth = 1
