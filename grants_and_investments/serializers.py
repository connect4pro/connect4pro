from django.db.models import fields
from rest_framework import serializers

from adverts.serializers import UserSerializer
from grants_and_investments.models import Grant, GrantComment, GrantTag
# Investment, InvestmentComment
from users.models import Connect4ProUser


class GrantCommentSerializer(serializers.ModelSerializer):
    """Grant comment serialize"""
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer()

    class Meta:
        model = GrantComment
        fields = ['id', 'post', 'text', 'user', 'posted']

    def create(self, validated_data):
        user = dict(validated_data.pop('user'))['id']
        post = validated_data['post']
        user = Connect4ProUser.objects.get(id=user)
        post = Grant.objects.get(id=post.id)
        text = validated_data['text']
        comment = GrantComment.objects.create(user=user, text=text, post=post)
        comment.save()
        return comment


# class InvestCommentSerializer(serializers.ModelSerializer):
#     """Grant comment serialize"""
#     id = serializers.IntegerField(read_only=True)
#     user = UserSerializer()
#
#     class Meta:
#         model = InvestmentComment
#         fields = ['id', 'post', 'text', 'user', 'posted']
#
#     def create(self, validated_data):
#         user = dict(validated_data.pop('user'))['id']
#         post = validated_data['post']
#         user = Connect4ProUser.objects.get(id=user)
#         post = Investment.objects.get(id=post.id)
#         text = validated_data['text']
#         comment = InvestmentComment.objects.create(user=user, text=text, post=post)
#         comment.save()
#         return comment

class GrantTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantTag
        fields = ('name',)


class GrantSerializer(serializers.ModelSerializer):
    """Grant serialize"""
    comments = GrantCommentSerializer(source='post_comment', many=True)
    tags = serializers.SerializerMethodField('get_tag_name', read_only=True)

    class Meta:
        model = Grant
        fields = (
            'id', 'name', 'sum', 'currency', 'deadline', 'description', 'location', 'period', 'logo', 'image',
            'created_at', 'comments', 'is_grant', 'is_invest', 'tags')
        depth = 1

    def get_tag_name(self, obj):
        return [f.name for f in obj.tag.all()]

# class InvestmentSerializer(serializers.ModelSerializer):
#     """Investment serialize"""
#     comments = InvestCommentSerializer(source='post_comment', many=True)
#
#     class Meta:
#         model = Investment
#         fields = (
#             'id', 'name', 'sum', 'currency', 'deadline', 'description', 'location', 'logo', 'image', 'period',
#             'created_at', 'comments')
#         depth = 1
