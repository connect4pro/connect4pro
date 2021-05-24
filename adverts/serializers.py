from rest_framework import serializers

from adverts.models import Category, UserAdvert


class CategorySerializer(serializers.ModelSerializer):
    """Category serialize"""
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'description']


class UserAdvertSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = UserAdvert
        fields = ['name', 'category', 'description', 'price', 'currency', 'completed', 'skills']
