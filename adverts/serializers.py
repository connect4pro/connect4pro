from rest_framework import serializers
from adverts.models import Category, BusinessAdvert, ProviderAdvert, ImageSet


class ImageSetSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = ImageSet
        fields = '__all__'

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
    images = ImageSetSerializer()
    class Meta:
        model = ProviderAdvert
        fields = '__all__'
        read_only_fields = ('user',)
