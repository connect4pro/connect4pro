from rest_framework import serializers

from adverts.models import Category, BusinessAdvert



class CategorySerializer(serializers.ModelSerializer):
    """Category serialize"""

    class Meta:
        model = Category
        fields = '__all__'


class UserAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessAdvert
        fields = '__all__'



