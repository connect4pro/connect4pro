from django.contrib.auth import authenticate
from users.models import Connect4ProUser, BusinessProfile, ProviderProfile
import os
import random
from rest_framework.exceptions import AuthenticationFailed


def register_social_user(provider, user_id, email, user_type=None):
    filtered_user_by_email = Connect4ProUser.objects.filter(email=email)

    if filtered_user_by_email.exists():

        if provider == filtered_user_by_email[0].auth_provider:

            registered_user = authenticate(
                email=email, password=os.environ.get('SOCIAL_SECRET'))

            return {
                'email': registered_user.email,
                'token': registered_user.tokens(),
                'id': registered_user.id}

        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

    else:
        user = {
            'email': email,
            'password': os.environ.get('SOCIAL_SECRET')}
        user = Connect4ProUser.objects.create_user(**user)
        user.is_active = True
        user.auth_provider = provider
        if user_type:
            if user_type == 'business':
                user.is_business = True
                profile = BusinessProfile.objects.create(user=user)
                profile.save()
            elif user_type == 'provider':
                user.is_provider = True
                profile = ProviderProfile.objects.create(user=user)
                profile.save()
        user.save()

        new_user = authenticate(
            email=email, password=os.environ.get('SOCIAL_SECRET'))
        return {
            'email': new_user.email,
            'tokens': new_user.tokens(),
            'id': new_user.id,
        }
