from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.models import Connect4ProUser, BusinessProfile, SectorChoices, ProviderProfile


class SectorChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorChoices
        fields = '__all__'


class BusinessProfileSerializer(serializers.ModelSerializer):
    sector = SectorChoicesSerializer(many=True)

    class Meta:
        model = BusinessProfile
        fields = (
            'first_name', 'last_name', 'region', 'turnover', 'employers', 'sector', 'demand', 'supply',)


class Connect4ProUserBPSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    business_profile = BusinessProfileSerializer(required=True)
    is_freemium = serializers.BooleanField(read_only=True)
    is_premium = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        user = Connect4ProUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = Connect4ProUser
        fields = (
            'id', 'email', 'password', 'company_name', 'facebook', 'instagram', 'site', 'is_freemium', 'is_premium',
            'business_profile')


class ProviderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProfile
        fields = ('manager', 'description', 'year', 'logo', 'address', 'services', 'scope')


class Connect4ProUserPPSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    provider_profile = ProviderProfileSerializer(required=True)
    is_freemium = serializers.BooleanField(read_only=True)
    is_premium = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        user = Connect4ProUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = Connect4ProUser
        fields = (
            'id', 'email', 'password', 'company_name', 'facebook', 'instagram', 'site', 'is_freemium', 'is_premium',
            'provider_profile')
