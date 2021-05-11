
from rest_framework.generics import ListAPIView, ListCreateAPIView


from adverts.models import Category, BusinessAdvert
from adverts.serializers import CategorySerializer, UserAdvertSerializer


class CategoryList(ListAPIView):
    """
    Список всех категорий.
    methods = GET
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BusinessAdvertList(ListCreateAPIView):
    """
    Список объявлений пользователя
    methods = GET, POST
    """
    queryset = BusinessAdvert.objects.all()
    serializer_class = UserAdvertSerializer





