from rest_framework import serializers

from adverts.serializers import UserSerializer
from blog.models import BlogPost, BlogComment
from users.models import Connect4ProUser


class BlogCommentSerializer(serializers.ModelSerializer):
    """Blog comment serialize"""
    user = UserSerializer()

    class Meta:
        model = BlogComment
        fields = ['id', 'post', 'text', 'user', 'posted']

    def create(self, validated_data):
        user = dict(validated_data.pop('user'))['id']
        post = validated_data['post']
        user = Connect4ProUser.objects.get(id=user)
        post = BlogPost.objects.get(id=post.id)
        text = validated_data['text']
        comment = BlogComment.objects.create(user=user, text=text, post=post)
        comment.save()
        return comment


class BlogPostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    comments = BlogCommentSerializer(source='post_comment', many=True, required=False)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'subtitle', 'description', 'created', 'post_image', 'comments']
        depth = 1
