from rest_framework import serializers
from blog.models import BlogPost, BlogComment


class BlogCommentSerializer(serializers.ModelSerializer):
    """Blog comment serialize"""

    class Meta:
        model = BlogComment
        fields = ['id', 'post', 'text', 'user']


class BlogPostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'subtitle', 'description', 'created', 'post_image', 'blog_comment']
        depth = 1
