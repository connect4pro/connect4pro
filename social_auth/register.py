from django.contrib.auth import authenticate
from users.models import Connect4ProUser
import os
import random
from rest_framework.exceptions import AuthenticationFailed


def register_social_user(provider, user_id, email):
    filtered_user_by_email = Connect4ProUser.objects.filter(email=email)

    if filtered_user_by_email.exists():

        if provider == filtered_user_by_email[0].auth_provider:

            registered_user = authenticate(
                email=email, password=os.environ.get('SOCIAL_SECRET'))

            return {
                'email': registered_user.email,
                'tokens': registered_user.tokens()}

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
        user.save()

        new_user = authenticate(
            email=email, password=os.environ.get('SOCIAL_SECRET'))
        return {
            'email': new_user.email,
            'tokens': new_user.tokens()
        }