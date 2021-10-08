from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from adverts.models import Category, BusinessAdvert, ProviderAdvert, BusinessAdvertComment, \
    ProviderAdvertComment, Image
from users.models import Connect4ProUser, ProviderProfile


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)

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

    def create(self, validated_data):
        user = dict(validated_data.pop('user'))['id']
        post = validated_data['post']
        user = Connect4ProUser.objects.get(id=user)
        post = BusinessAdvert.objects.get(id=post.id)
        text = validated_data['text']
        comment = BusinessAdvertComment.objects.create(user=user, text=text, post=post)
        comment.save()
        return comment


class ProviderAdvertCommentSerializer(serializers.ModelSerializer):
    # text = serializers.CharField(required=False)
    # post = serializers.IntegerField(required=False)
    user = UserSerializer(required=False)

    class Meta:
        model = ProviderAdvertComment
        fields = ['id', 'post', 'text', 'user', 'posted']

    def create(self, validated_data):
        user = dict(validated_data.pop('user'))['id']
        post = validated_data['post']
        user = Connect4ProUser.objects.get(id=user)
        post = ProviderAdvert.objects.get(id=post.id)
        text = validated_data['text']
        comment = ProviderAdvertComment.objects.create(user=user, text=text, post=post)
        comment.save()
        return comment


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Image
        fields = ('image',)


# class ImageSetSerializer(serializers.ModelSerializer):
#     album = ImageSerializer(source='images', many=True, required=False)
#
#     class Meta:
#         model = Album
#         fields = ('album',)


class AdvertCategorySerializer(serializers.ModelSerializer):
    """Category serialize"""

    class Meta:
        model = Category
        fields = '__all__'


class UserAdvertSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    phone = serializers.CharField(required=False)
    telegram = serializers.CharField(required=False)

    class Meta:
        model = Connect4ProUser
        fields = ('id', 'phone', 'telegram')


class BusinessAdvertSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    comments = BusinessAdvertCommentSerializer(source='post_comment', many=True, required=False, read_only=True)
    user = UserAdvertSerializer(required=False)

    class Meta:
        model = BusinessAdvert
        fields = ['id', 'title', 'description', 'price', 'currency', 'completed', 'user', 'needs',
                  'suggest', 'tel', 'created_at', 'comments']
        depth = 1

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        user = Connect4ProUser.objects.get(id=user_data['id'])
        advert = BusinessAdvert.objects.create(**validated_data, user=user.business_profile)
        advert.save()
        return advert


class ProviderAdvertSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    id = serializers.IntegerField(read_only=True, required=False)
    comments = ProviderAdvertCommentSerializer(source='post_comment', many=True, required=False, read_only=True)
    images = ImageSerializer(source='images_set', many=True, required=False)
    # images = ImageSetSerializer(required=False)
    # user = UserAdvertSerializer(required=False)
    user = serializers.IntegerField(required=False)

    class Meta:
        model = ProviderAdvert
        fields = (
            'id', 'images', 'title', 'description', 'price', 'currency', 'tel', 'scope', 'services',
            'location', 'created_at', 'user', 'foundation_date', 'comments')
        depth = 1

    def create(self, validated_data):
        user = validated_data.pop('user')
        user_id = ProviderProfile.objects.get(user_id=user)
        images_data = self.context.get('view').request.FILES
        advert = ProviderAdvert.objects.create(**validated_data, user=user_id.id)
        for image_data in images_data.values():
            Image.objects.create(advert=advert, image=image_data)

        return advert
