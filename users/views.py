from abc import ABC

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import Connect4ProUser, Sector, Knowledge, Skill, Method
from users.permissions import IsOwnerOrReadOnly, PremiumPermission
from users.serializers import SectorSerializer, UserBusinessProfileSerializer, \
    UserProviderProfileSerializer, UpdateProviderProfile, UpdateBusinessProfile, SkillSerializer, KnowledgeSerializer, \
    MethodSerializer, ChangePasswordSerializer


class BusinessUserList(ListAPIView):
    queryset = Connect4ProUser.objects.filter(is_business=True)
    serializer_class = UserBusinessProfileSerializer


class BusinessUserRegister(CreateAPIView):
    serializer_class = UserBusinessProfileSerializer


class ProviderUserList(ListAPIView):
    queryset = Connect4ProUser.objects.filter(is_provider=True)
    serializer_class = UserProviderProfileSerializer


class ProviderUserRegister(CreateAPIView):
    serializer_class = UserProviderProfileSerializer


class BusinessUserUpdate(UpdateAPIView):
    queryset = Connect4ProUser.objects.filter(is_business=True)
    serializer_class = UpdateBusinessProfile
    lookup_field = 'id'
    parser_classes = [MultiPartParser, FormParser]

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []

        return super().get_parsers()


class ProviderUserUpdate(UpdateAPIView):
    queryset = Connect4ProUser.objects.filter(is_provider=True)
    serializer_class = UpdateProviderProfile
    lookup_field = 'id'
    parser_classes = [MultiPartParser, FormParser]

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []

        return super().get_parsers()


class BusinessProfileDetail(RetrieveAPIView):
    serializer_class = UserBusinessProfileSerializer
    queryset = Connect4ProUser.objects.filter(is_business=True)
    lookup_field = 'id'


class ProviderProfileDetail(RetrieveAPIView):
    serializer_class = UserProviderProfileSerializer
    queryset = Connect4ProUser.objects.filter(is_provider=True)
    lookup_field = 'id'


class SectorList(ListAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer


class SkillList(ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class KnowledgeList(ListAPIView):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializer


class MethodList(ListAPIView):
    queryset = Method.objects.all()
    serializer_class = MethodSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        user = authenticate(**attrs)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['id'] = self.user.id
        data['email'] = self.user.email
        if self.user.is_business:
            data['user_type'] = 'business'
        elif self.user.is_provider:
            data['user_type'] = 'provider'
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = Connect4ProUser

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
