from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from adverts.models import Category, BusinessAdvert, ProviderAdvert, Album, BusinessAdvertComment, \
    ProviderAdvertComment, Image
from users.models import Connect4ProUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect4ProUser
        fields = ['id', 'avatar', 'first_name', 'last_name']


class BusinessAdvertCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = BusinessAdvertComment
        fields = ['id', 'post', 'text', 'user', 'posted']


class ProviderAdvertCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ProviderAdvertComment
        fields = ['id', 'post', 'text', 'user', 'posted']

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Image
        fields = ('image',)

class ImageSetSerializer(serializers.ModelSerializer):
    image_set = ImageSerializer(source='images', many=True)
    class Meta:
        model = Album
        fields = ('image_set',)


class AdvertCategorySerializer(serializers.ModelSerializer):
    """Category serialize"""

    class Meta:
        model = Category
        fields = '__all__'


class BusinessAdvertSerializer(serializers.ModelSerializer):
    comments = BusinessAdvertCommentSerializer(source='post_comment', many=True)
    class Meta:
        model = BusinessAdvert
        fields = ['id', 'title', 'category', 'description', 'price', 'currency', 'completed', 'user', 'needs',
                  'suggest', 'tel', 'created_at', 'comments']
        depth = 1


class ProviderAdvertSerializer(serializers.ModelSerializer):
    comments = ProviderAdvertCommentSerializer(source='post_comment', many=True)
    images = ImageSetSerializer()

    class Meta:
        model = ProviderAdvert
        fields = (
            'id', 'images', 'title', 'description', 'price', 'currency', 'category', 'created_at', 'comments')
        depth = 1
