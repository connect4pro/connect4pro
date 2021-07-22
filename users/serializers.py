from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from serializer_permissions import serializers
from rest_framework.authtoken.models import Token
from .permissions import PremiumPermission, IsOwner
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import Connect4ProUser, BusinessProfile, Sector, ProviderProfile, Skill, Knowledge, Method


class SectorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(permission_classes=(PremiumPermission,), required=False)

    class Meta:
        model = Sector
        fields = ('id', 'name',)


class SkillSerializer(serializers.ModelSerializer):
    name = serializers.CharField(permission_classes=(PremiumPermission,), required=False)

    class Meta:
        model = Skill
        fields = ('id', 'name',)


class KnowledgeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(permission_classes=(PremiumPermission,), required=False)

    class Meta:
        model = Knowledge
        fields = ('id', 'name',)


class MethodSerializer(serializers.ModelSerializer):
    name = serializers.CharField(permission_classes=(PremiumPermission,), required=False)

    class Meta:
        model = Method
        fields = ('id', 'name',)


class BusinessProfileSerializer(serializers.ModelSerializer):
    turnover = serializers.CharField(permission_classes=(PremiumPermission,), required=False)
    employers = serializers.IntegerField(permission_classes=(PremiumPermission,), required=False)
    category = serializers.CharField(permission_classes=(PremiumPermission,), required=False)
    sector = SectorSerializer(permission_classes=(PremiumPermission,), many=True, required=False)

    class Meta:
        model = BusinessProfile
        fields = ('sector', 'turnover', 'employers', 'category')


class UserBusinessProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, permission_classes=(PremiumPermission,))
    last_name = serializers.CharField(required=True, permission_classes=(PremiumPermission,))
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    business_profile = BusinessProfileSerializer(required=False)
    is_premium = serializers.BooleanField(read_only=True)
    is_business = serializers.BooleanField(read_only=True)
    is_provider = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        profile_data = validated_data.pop('business_profile')

        sector_data = profile_data.pop('sector')
        if validated_data['password'] != validated_data['password2']:
            raise ValidationError('Passwords must match')
        else:
            validated_data.pop('password2')
            user = Connect4ProUser.objects.create_user(**validated_data)
            user.is_business = True
            user.save()
        profile = BusinessProfile.objects.create(user=user, **profile_data)

        for sect in sector_data:
            try:
                sector = get_object_or_404(Sector, name=sect['name'])
                profile.save()
                profile.sector.add(sector)
            except:
                continue
            finally:
                profile.save()
        return user

    class Meta:
        model = Connect4ProUser
        fields = (
            'id', 'email', 'password', 'password2', 'first_name', 'last_name', 'birth_date', 'gender', 'country',
            'city', 'phone', 'telegram', 'avatar', 'site', 'is_premium', 'is_business', 'is_provider',
            'business_profile')


class ProviderProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(permission_classes=(PremiumPermission,), many=True, required=False)
    knowledge = KnowledgeSerializer(permission_classes=(PremiumPermission,), many=True, required=False)
    methods = MethodSerializer(permission_classes=(PremiumPermission,), many=True, required=False)

    class Meta:
        model = ProviderProfile
        fields = ('skills', 'knowledge', 'methods')


class UserProviderProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, permission_classes=(PremiumPermission,))
    last_name = serializers.CharField(required=True, permission_classes=(PremiumPermission,))
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    provider_profile = ProviderProfileSerializer(required=False)
    is_premium = serializers.BooleanField(read_only=True)
    is_business = serializers.BooleanField(read_only=True)
    is_provider = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        profile_data = validated_data.pop('provider_profile')
        skills_data = profile_data.pop('skills')
        knowledge_data = profile_data.pop('knowledge')
        methods_data = profile_data.pop('methods')

        if validated_data['password'] != validated_data['password2']:
            raise ValidationError('Passwords must match')
        else:
            validated_data.pop('password2')
            user = Connect4ProUser.objects.create_user(**validated_data)
            user.is_provider = True
            user.save()
        profile = ProviderProfile.objects.create(user=user, **profile_data)

        for method in methods_data:
            try:
                method_obj = get_object_or_404(Method, name=method['name'])
                profile.save()
                profile.methods.add(method_obj)
            except:
                continue

        for knw in knowledge_data:
            try:
                knw_obj = get_object_or_404(Knowledge, name=knw['name'])
                profile.save()
                profile.knowledge.add(knw_obj)
            except:
                continue

        for skill in skills_data:
            try:
                skill_obj = get_object_or_404(Skill, name=skill['name'])
                profile.save()
                profile.skills.add(skill_obj)
            except:
                continue

        profile.save()
        return user

    class Meta:
        model = Connect4ProUser
        fields = (
            'id', 'email', 'password', 'password2', 'first_name', 'last_name', 'birth_date', 'gender', 'country',
            'city', 'phone', 'telegram', 'avatar', 'site', 'is_premium', 'is_business', 'is_provider',
            'provider_profile')


class UpdateBusinessProfile(serializers.ModelSerializer):
    business_profile = BusinessProfileSerializer(required=False)

    class Meta:
        model = Connect4ProUser
        fields = ('first_name', 'last_name', 'birth_date', 'gender', 'country',
                  'city', 'phone', 'telegram', 'avatar', 'site', 'business_profile')

    def update(self, instance, validated_data):
        instance.__dict__.update(validated_data)
        instance.save()

        return instance


class UpdateProviderProfile(serializers.ModelSerializer):
    provider_profile = ProviderProfileSerializer(required=True)

    class Meta:
        model = Connect4ProUser
        fields = ('first_name', 'last_name', 'birth_date', 'gender', 'country',
                  'city', 'phone', 'telegram', 'avatar', 'site', 'provider_profile')

    def update(self, instance, validated_data):
        instance.__dict__.update(validated_data)
        instance.save()

        return instance
