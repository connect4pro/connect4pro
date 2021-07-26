from rest_framework import serializers
from adverts.models import Category, BusinessAdvert, ProviderAdvert, Album


class ImageSetSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Album
        fields = ('image',)

class AdvertCategorySerializer(serializers.ModelSerializer):
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
        fields = ('images', 'title', 'description', 'price', 'currency', 'category')
        read_only_fields = ('user',)
