from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, get_object_or_404
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
    MethodSerializer


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
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = UpdateBusinessProfile
    lookup_field = 'id'


class ProviderUserUpdate(UpdateAPIView):
    queryset = Connect4ProUser.objects.filter(is_provider=True)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = UpdateProviderProfile
    lookup_field = 'id'


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