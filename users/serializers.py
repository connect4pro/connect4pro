from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from serializer_permissions import serializers
from rest_framework.authtoken.models import Token
from .permissions import PremiumPermission
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import Connect4ProUser, BusinessProfile, Sector, ProviderProfile


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ('description',)


class BusinessProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(permission_classes=(PremiumPermission,))
    last_name = serializers.CharField(permission_classes=(PremiumPermission,))
    region = serializers.CharField(permission_classes=(PremiumPermission,))
    turnover = serializers.CharField(permission_classes=(PremiumPermission,))
    employers = serializers.IntegerField(permission_classes=(PremiumPermission,))
    sector = SectorSerializer(permission_classes=(PremiumPermission,), many=True)

    class Meta:
        model = BusinessProfile
        fields = (
            'first_name', 'last_name', 'region', 'turnover', 'employers', 'sector', 'demand', 'supply',)


class Connect4ProUserBPSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    business_profile = BusinessProfileSerializer(required=True)
    is_premium = serializers.BooleanField(read_only=True)
    # avatar = serializers.SerializerMethodField('get_avatar_url')
    avatar = serializers.ImageField(required=False, allow_empty_file=True)

    def create(self, validated_data):
        print(validated_data)
        profile_data = validated_data.pop('business_profile')
        sector_data = profile_data.pop('sector')
        if validated_data['password'] != validated_data['password2']:
            raise ValidationError('Passwords must match')
        else:
            validated_data.pop('password2')
            user = Connect4ProUser.objects.create_user(
                **validated_data)
        profile = BusinessProfile.objects.create(user=user, **profile_data)

        for sect in sector_data:
            sector = get_object_or_404(Sector, description=sect['description'])
            profile.save()
            profile.sector.add(sector)
        return user


    class Meta:
        model = Connect4ProUser
        fields = (
            'id', 'email', 'password', 'password2', 'avatar', 'company_name', 'facebook', 'instagram', 'site',
            'is_premium',
            'business_profile')


class ProviderProfileSerializer(serializers.ModelSerializer):
    manager = serializers.CharField(permission_classes=(PremiumPermission,))
    description = serializers.CharField(permission_classes=(PremiumPermission,))
    year = serializers.DateField(permission_classes=(PremiumPermission,))
    address = serializers.CharField(permission_classes=(PremiumPermission,))

    class Meta:
        model = ProviderProfile
        fields = ('manager', 'description', 'year', 'logo', 'address', 'services', 'scope')


class Connect4ProUserPPSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    provider_profile = ProviderProfileSerializer(required=True)
    is_premium = serializers.BooleanField(read_only=True)
    # avatar = serializers.SerializerMethodField('get_avatar_url')
    avatar = serializers.ImageField(required=False, allow_empty_file=True)

    def create(self, validated_data):

        profile_data = validated_data.pop('provider_profile')
        if validated_data['password'] != validated_data['password2']:
            raise ValidationError('Passwords must match')
        else:
            validated_data.pop('password2')
            user = Connect4ProUser.objects.create_user(
                **validated_data)
        ProviderProfile.objects.create(user=user, **profile_data)
        return user


    class Meta:
        model = Connect4ProUser
        fields = (
            'id', 'email', 'password', 'password2', 'avatar', 'company_name', 'facebook', 'instagram', 'site',
            'is_premium',
            'provider_profile')


class UpdateBusinessProfile(serializers.ModelSerializer):
    business_profile = BusinessProfileSerializer(required=True)

    class Meta:
        model = Connect4ProUser
        fields = ('company_name', 'facebook', 'avatar', 'instagram', 'site', 'business_profile')

    def update(self, instance, validated_data):
        instance.company_name = validated_data['company_name']
        instance.facebook = validated_data['facebook']
        instance.instagram = validated_data['instagram']
        instance.site = validated_data['site']
        instance.business_profile = validated_data['business_profile']
        instance.save()

        return instance


class UpdateProviderProfile(serializers.ModelSerializer):
    provider_profile = ProviderProfileSerializer(required=True)

    class Meta:
        model = Connect4ProUser
        fields = ('company_name', 'facebook', 'avatar', 'instagram', 'site', 'provider_profile')

    def update(self, instance, validated_data):
        instance.company_name = validated_data['company_name']
        instance.facebook = validated_data['facebook']
        instance.instagram = validated_data['instagram']
        instance.site = validated_data['site']
        instance.business_profile = validated_data['provider_profile']
        instance.save()

        return instance
