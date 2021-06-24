from rest_framework import permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView

from adverts.models import Category, BusinessAdvert, ProviderAdvert
from adverts.permissions import IsOwnerOrReadOnly
from adverts.serializers import AdvertCategorySerializer, BusinessAdvertSerializer, ProviderAdvertSerializer


class CategoryList(ListAPIView):
    """
    Список всех категорий.
    methods = GET
    """
    queryset = Category.objects.all()
    serializer_class = AdvertCategorySerializer


class BusinessAdvertList(ListCreateAPIView):
    """
    Список объявлений МСБ
    methods = GET, POST
    """
    queryset = BusinessAdvert.objects.all()
    serializer_class = BusinessAdvertSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.business_profile)


class ProviderAdvertList(ListCreateAPIView):
    """
    Список объявлений Консультантов
    methods = GET, POST
    """
    queryset = ProviderAdvert.objects.all()
    serializer_class = ProviderAdvertSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.provider_profile)


class BusinessAdvertUpdate(UpdateAPIView):
    serializer_class = BusinessAdvertSerializer
    lookup_field = 'id'
    queryset = BusinessAdvert.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user.business_profile)


class ProviderAdvertUpdate(UpdateAPIView):
    serializer_class = ProviderAdvertSerializer
    lookup_field = 'id'
    queryset = ProviderAdvert.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user.provider_profile)
