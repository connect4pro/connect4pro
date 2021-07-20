from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import Connect4ProUser, Sector, Knowledge, Skill, Method
from users.permissions import IsOwnerOrReadOnly
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
