from django.db.models import fields
from rest_framework import serializers
from grants_and_investments.models import Grant, Investment, GrantComment, InvestmentComment


class GrantCommentSerializer(serializers.ModelSerializer):
    """Grant comment serialize"""
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = GrantComment
        fields = ['id', 'grant', 'commentator_text', 'commentator_name', 'commentator_email']
        read_only_fields = ('user',)


class InvestCommentSerializer(serializers.ModelSerializer):
    """Grant comment serialize"""
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = InvestmentComment
        fields = ['id', 'investment', 'commentator_text', 'commentator_name', 'commentator_email']
        read_only_fields = ('user',)


class GrantSerializer(serializers.ModelSerializer):
    """Grant serialize"""

    class Meta:
        model = Grant
        fields = (
            'id', 'grant_name', 'grant_sum', 'currency', 'grant_deadline', 'grant_description', 'location', 'period',
            'grant_comment')
        read_only_fields = ('user',)
        depth = 1


class InvestmentSerializer(serializers.ModelSerializer):
    """Investment serialize"""

    class Meta:
        model = Investment
        fields = (
            'id', 'invest_name', 'invest_sum', 'currency', 'invest_deadline', 'invest_description', 'location',
            'period', 'invest_comment')
        read_only_fields = ('user',)
        depth = 1
