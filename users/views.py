from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView

from users.models import BusinessProfile, Connect4ProUser
from users.serializers import Connect4ProUserBPSerializer, BusinessProfileSerializer, Connect4ProUserPPSerializer


class BusinessUserList(ListAPIView):
    queryset = Connect4ProUser.objects.filter()
    serializer_class = Connect4ProUserBPSerializer

    # def get_serializer_class(self):
    #     pass


class BusinessUserRegister(CreateAPIView):
    serializer_class = Connect4ProUserBPSerializer


class ProviderUserList(ListAPIView):
    queryset = Connect4ProUser.objects.filter()
    serializer_class = Connect4ProUserPPSerializer


class ProviderUserRegister(CreateAPIView):
    serializer_class = Connect4ProUserPPSerializer
