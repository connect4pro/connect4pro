from django.db.models import fields
from rest_framework import serializers
from grants_and_investments.models import Grant, Investment

class GrantSerializer(serializers.ModelSerializer):
    """Grant serialize"""
    class Meta:
        model = Grant
        fields = ('grant_name', 'grant_sum', 'grant_deadline', 'grant_description')


class InvestmentSerializer(serializers.ModelSerializer):
    """Investment serialize"""
    class Meta:
        model = Investment
        fields = ('invest_name', 'invest_sum', 'invest_deadline', 'invest_description')