from django.db.models import fields
from rest_framework import serializers
from grants_and_investments.models import Grant, Investment, GrantInvestmentComment


class GrantSerializer(serializers.ModelSerializer):
    """Grant serialize"""

    class Meta:
        model = Grant
        fields = (
        'id', 'grant_name', 'grant_sum', 'currency', 'grant_deadline', 'grant_description', 'location', 'period')
        read_only_fields = ('user',)


class InvestmentSerializer(serializers.ModelSerializer):
    """Investment serialize"""

    class Meta:
        model = Investment
        fields = (
        'id', 'invest_name', 'invest_sum', 'currency', 'invest_deadline', 'invest_description', 'location', 'period')
        read_only_fields = ('user',)


class GrantInvestmentCommentSerializer(serializers.ModelSerializer):
    """Grant and Investment comment serialize"""
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = GrantInvestmentComment
        fields = '__all__'
        read_only_fields = ('user',)
