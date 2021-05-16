from rest_framework import serializers
from adverts.models import Category, BusinessAdvert, ProviderAdvert


class CategorySerializer(serializers.ModelSerializer):
    """Category serialize"""

    class Meta:
        model = Category
        fields = '__all__'


class BusinessAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessAdvert
        fields = '__all__'
        read_only_fields = ('user',)


class ProviderAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderAdvert
        fields = '__all__'
        read_only_fields = ('user',)
