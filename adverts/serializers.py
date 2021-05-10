from rest_framework import serializers

from adverts.models import Category, UserAdvert
from blog.models import BlogPost


class CategorySerializer(serializers.ModelSerializer):
    """Category serialize"""

    class Meta:
        model = Category
        fields = '__all__'


class UserAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdvert
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
