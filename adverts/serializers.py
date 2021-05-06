from rest_framework import serializers

from adverts.models import Category, UserAdvert


class CategorySerializer(serializers.ModelSerializer):
    """Category serialize"""
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class UserAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdvert
        fields = '__all__'
