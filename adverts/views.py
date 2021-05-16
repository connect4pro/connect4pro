from rest_framework.generics import ListAPIView, ListCreateAPIView

from adverts.models import Category, BusinessAdvert, ProviderAdvert
from adverts.serializers import CategorySerializer, BusinessAdvertSerializer, ProviderAdvertSerializer


class CategoryList(ListAPIView):
    """
    Список всех категорий.
    methods = GET
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BusinessAdvertList(ListCreateAPIView):
    """
    Список объявлений МСБ
    methods = GET, POST
    """
    queryset = BusinessAdvert.objects.all()
    serializer_class = BusinessAdvertSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProviderAdvertList(ListCreateAPIView):
    """
    Список объявлений Консультантов
    methods = GET, POST
    """
    queryset = ProviderAdvert.objects.all()
    serializer_class = ProviderAdvertSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
