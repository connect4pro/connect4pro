from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from adverts.models import Category, BusinessAdvert, ProviderAdvert, Album, BusinessAdvertComment, \
    ProviderAdvertComment, Image
from users.models import Connect4ProUser, ProviderProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect4ProUser
        fields = ['id', 'avatar', 'first_name', 'last_name']


class BusinessAdvertCommentSerializer(serializers.ModelSerializer):
    # text = serializers.CharField(required=False)
    # post = serializers.IntegerField(required=False)
    user = UserSerializer(required=False)

    class Meta:
        model = BusinessAdvertComment
        fields = ['id', 'post', 'text', 'user', 'posted']


class ProviderAdvertCommentSerializer(serializers.ModelSerializer):
    # text = serializers.CharField(required=False)
    # post = serializers.IntegerField(required=False)
    user = UserSerializer(required=False)

    class Meta:
        model = ProviderAdvertComment
        fields = ['id', 'post', 'text', 'user', 'posted']


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Image
        fields = ('image',)


class ImageSetSerializer(serializers.ModelSerializer):
    image_set = ImageSerializer(source='images', many=True, required=False)

    class Meta:
        model = Album
        fields = ('image_set',)


class AdvertCategorySerializer(serializers.ModelSerializer):
    """Category serialize"""

    class Meta:
        model = Category
        fields = '__all__'


class BusinessAdvertSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    comments = BusinessAdvertCommentSerializer(source='post_comment', many=True, required=False)

    class Meta:
        model = BusinessAdvert
        fields = ['id', 'title', 'category', 'description', 'price', 'currency', 'completed', 'user', 'needs',
                  'suggest', 'tel', 'created_at', 'comments']
        depth = 1


class UserAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect4ProUser
        fields = ('id', 'phone', 'telegram')


class ProviderProfileAdvertSerializer(serializers.Serializer):
    class Meta:
        model = ProviderProfile
        fields = ('foundation_date',)


class ProviderAdvertSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    comments = ProviderAdvertCommentSerializer(source='post_comment', many=True, required=False)
    images = ImageSetSerializer(required=False)
    user = UserAdvertSerializer(required=False)
    found_date = ProviderProfileAdvertSerializer(required=False, read_only=True)

    class Meta:
        model = ProviderAdvert
        fields = (
            'id', 'images', 'title', 'description', 'price', 'currency', 'category', 'tel', 'scope', 'services',
            'location', 'created_at', 'user', 'found_date', 'comments')
        depth = 1
