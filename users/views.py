from django.shortcuts import render, redirect

from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import BusinessProfile, Connect4ProUser
from users.permissions import IsOwnerOrReadOnly
from users.serializers import Connect4ProUserBPSerializer, BusinessProfileSerializer, Connect4ProUserPPSerializer, \
    UpdateBusinessProfile, UpdateProviderProfile



class BusinessUserList(ListAPIView):
    queryset = Connect4ProUser.objects.filter(business_profile__as_business=True)
    serializer_class = Connect4ProUserBPSerializer


class BusinessUserRegister(CreateAPIView):
    serializer_class = Connect4ProUserBPSerializer

    def post(self, *args, **kwargs):
        super().post(*args, **kwargs)
        return redirect('users:business')


class ProviderUserList(ListAPIView):
    queryset = Connect4ProUser.objects.filter(provider_profile__as_provider=True)
    serializer_class = Connect4ProUserPPSerializer


class ProviderUserRegister(CreateAPIView):
    serializer_class = Connect4ProUserPPSerializer


class BusinessProfileDetail(RetrieveAPIView):
    serializer_class = Connect4ProUserBPSerializer
    queryset = Connect4ProUser.objects.all()
    lookup_field = 'id'


class ProviderProfileDetail(RetrieveAPIView):
    serializer_class = Connect4ProUserPPSerializer
    queryset = Connect4ProUser.objects.all()
    lookup_field = 'id'


class UpdateBusinessProfileView(UpdateAPIView):
    queryset = Connect4ProUser.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = UpdateBusinessProfile
    lookup_field = 'id'


class UpdateProviderProfileView(UpdateAPIView):
    queryset = Connect4ProUser.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = UpdateProviderProfile
    lookup_field = 'id'


def facebook_auth(request):

    return render(request, 'facebook.html')


def google_auth(request):

    return render(request, 'google.html')

