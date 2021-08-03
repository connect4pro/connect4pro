from rest_framework import serializers
from adverts.models import Category, BusinessAdvert, ProviderAdvert, Album, BusinessAdvertComment, ProviderAdvertComment


class BusinessAdvertCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessAdvertComment
        fields = ['id', 'post', 'text', 'user']


class ProviderAdvertCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderAdvertComment
        fields = ['id', 'post', 'text', 'user']


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
        fields = ['id', 'title', 'category', 'description', 'price', 'currency', 'completed', 'user', 'needs',
                  'suggest', 'tel', 'created_at', 'post_comment']
        depth = 1


class ProviderAdvertSerializer(serializers.ModelSerializer):
    images = ImageSetSerializer()

    class Meta:
        model = ProviderAdvert
        fields = (
            'id', 'images', 'title', 'description', 'price', 'currency', 'category', 'created_at', 'post_comment')
        depth = 1
