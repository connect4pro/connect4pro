
from rest_framework.generics import ListAPIView, ListCreateAPIView


from adverts.models import Category, UserAdvert
from adverts.serializers import CategorySerializer, UserAdvertSerializer, BlogPostSerializer


class CategoryList(ListAPIView):
    """
    Список всех категорий.
    methods = GET
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserAdvertList(ListCreateAPIView):
    """
    Список объявлений пользователя
    methods = GET, POST
    """
    queryset = UserAdvert.objects.all()
    serializer_class = UserAdvertSerializer





