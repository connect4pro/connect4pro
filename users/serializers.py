from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from serializer_permissions import serializers
from rest_framework.authtoken.models import Token
from .permissions import PremiumPermission, IsOwner
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import Connect4ProUser, BusinessProfile, Sector, ProviderProfile, Skill, Knowledge, Method


class SectorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)

    class Meta:
        model = Sector
        fields = ('name',)


class SkillSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)

    class Meta:
        model = Skill
        fields = ('name',)


class KnowledgeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)

    class Meta:
        model = Knowledge
        fields = ('name',)


class MethodSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)

    class Meta:
        model = Method
        fields = ('name',)


class BusinessProfileSerializer(serializers.ModelSerializer):
    turnover = serializers.CharField(required=False)
    employers = serializers.IntegerField(required=False)
    category = serializers.CharField(required=False)
    sector = SectorSerializer(many=True, required=False)

    class Meta:
        model = BusinessProfile
        fields = ('sector', 'turnover', 'employers', 'category')


class UserBusinessProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
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
                sector = Sector.objects.get(name=sect['name'])
                if sector:
                    profile.save()
                    profile.sector.add(sector)
                else:
                    sector_obj = Sector.objects.create(name=dict(sect)['name'])
                    profile.save()
                    profile.sector.add(sector_obj)
            except:
                continue
            finally:
                profile.save()
        return user

    class Meta:
        model = Connect4ProUser
        fields = (
            'id', 'email', 'password', 'password2', 'first_name', 'last_name', 'birth_date', 'gender', 'country',
            'city', 'phone', 'telegram', 'avatar', 'site', 'is_premium', 'start_date', 'end_date', 'is_business',
            'is_provider',
            'business_profile')


class ProviderProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(required=False, many=True)
    knowledge = KnowledgeSerializer(many=True, required=False)
    methods = MethodSerializer(many=True, required=False)

    class Meta:
        model = ProviderProfile
        fields = ('skills', 'knowledge', 'methods')


class UserProviderProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
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
                method_obj = Method.objects.get(name=method['name'])
                profile.save()
                profile.methods.add(method_obj)
            except:
                continue

        for knw in knowledge_data:
            try:
                knw_obj = Knowledge.objects.get(name=knw['name'])
                profile.save()
                profile.knowledge.add(knw_obj)
            except:
                continue

        for skill in skills_data:
            try:

                skill_obj = Skill.objects.create(name=dict(skill)['name'])

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
            'city', 'phone', 'telegram', 'avatar', 'site', 'is_premium', 'start_date', 'end_date', 'is_business',
            'is_provider',
            'provider_profile')


class UpdateBusinessProfile(serializers.ModelSerializer):
    # business_profile = BusinessProfileSerializer(required=False)
    avatar = serializers.ImageField(required=False)

    class Meta:
        model = Connect4ProUser
        fields = ('email', 'avatar', 'first_name', 'last_name', 'birth_date', 'gender', 'country',
                  'city', 'phone', 'telegram', 'avatar', 'site')# 'business_profile')

    def update(self, instance, validated_data):
        instance.__dict__.update(validated_data)
        instance.save()

        return instance


class UpdateProviderProfile(serializers.ModelSerializer):
    # provider_profile = ProviderProfileSerializer(required=True)
    avatar = serializers.ImageField(required=False)

    class Meta:
        model = Connect4ProUser
        fields = ('email', 'avatar', 'first_name', 'last_name', 'birth_date', 'gender', 'country',
                  'city', 'phone', 'telegram', 'avatar', 'site') #'provider_profile')

    def update(self, instance, validated_data):
        instance.__dict__.update(validated_data)
        instance.save()

        return instance



class ChangePasswordSerializer(serializers.Serializer):
    model = Connect4ProUser

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)