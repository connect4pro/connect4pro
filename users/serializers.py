from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.models import Connect4ProUser, BusinessProfile, Sector, ProviderProfile


class SectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = ('description',)


class BusinessProfileSerializer(serializers.ModelSerializer):
    sector = SectorSerializer(many=True)

    class Meta:
        model = BusinessProfile
        fields = (
            'first_name', 'last_name', 'region', 'turnover', 'employers', 'sector', 'demand', 'supply',)



class Connect4ProUserBPSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    business_profile = BusinessProfileSerializer(required=True)
    is_premium = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        profile_data = validated_data.pop('business_profile')

        sector_data = profile_data.pop('sector')

        user = Connect4ProUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        profile = BusinessProfile.objects.create(user=user, **profile_data)

        for sect in sector_data:
            sector = get_object_or_404(Sector, description=sect['description'])
            profile.save()
            profile.sector.add(sector)
        return user

    class Meta:
        model = Connect4ProUser
        fields = (
            'id', 'email', 'password', 'company_name', 'facebook', 'instagram', 'site', 'is_premium',
            'business_profile')



class ProviderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProfile
        fields = ('manager', 'description', 'year', 'logo', 'address', 'services', 'scope')


class Connect4ProUserPPSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    provider_profile = ProviderProfileSerializer(required=True)
    is_premium = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        profile_data = validated_data.pop('provider_profile')
        user = Connect4ProUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        ProviderProfile.objects.create(user=user, **profile_data)
        return user

    class Meta:
        model = Connect4ProUser
        fields = (
            'id', 'email', 'password', 'company_name', 'facebook', 'instagram', 'site', 'is_premium',
            'provider_profile')
