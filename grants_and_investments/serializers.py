from django.db.models import fields
from rest_framework import serializers
from grants_and_investments.models import Grant, Investment, GrantComment, InvestmentComment


class GrantCommentSerializer(serializers.ModelSerializer):
    """Grant comment serialize"""
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = GrantComment
        fields = ['id', 'post', 'text', 'user', 'posted']


class InvestCommentSerializer(serializers.ModelSerializer):
    """Grant comment serialize"""
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = InvestmentComment
        fields = ['id', 'post', 'text', 'user', 'posted']


class GrantSerializer(serializers.ModelSerializer):
    """Grant serialize"""

    class Meta:
        model = Grant
        fields = (
            'id', 'name', 'sum', 'currency', 'deadline', 'description', 'location', 'period', 'logo', 'image',
            'created_at', 'post_comment')
        depth = 1


class InvestmentSerializer(serializers.ModelSerializer):
    """Investment serialize"""

    class Meta:
        model = Investment
        fields = (
            'id', 'name', 'sum', 'currency', 'deadline', 'description', 'location', 'logo', 'image', 'period',
            'created_at', 'post_comment')
        depth = 1
