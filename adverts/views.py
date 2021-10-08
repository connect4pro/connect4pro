from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FormParser

from adverts.models import Category, BusinessAdvert, ProviderAdvert, BusinessAdvertComment, ProviderAdvertComment
from adverts.permissions import IsOwnerOrReadOnly
from adverts.serializers import AdvertCategorySerializer, BusinessAdvertSerializer, ProviderAdvertSerializer, \
    BusinessAdvertCommentSerializer, ProviderAdvertCommentSerializer


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

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user.business_profile)


class ProviderAdvertList(ListCreateAPIView):
    """
    Список объявлений Консультантов
    methods = GET, POST
    """
    queryset = ProviderAdvert.objects.all()
    serializer_class = ProviderAdvertSerializer
    parser_classes = [MultiPartParser, FormParser]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user.provider_profile)
    #
    # def post(self, request, *args, **kwargs):


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


class BusinessAdvertCommentCreate(CreateAPIView):
    serializer_class = BusinessAdvertCommentSerializer


class ProviderAdvertCommentCreate(CreateAPIView):
    serializer_class = ProviderAdvertCommentSerializer


class BusinessAdvertCommentList(ListAPIView):
    queryset = BusinessAdvertComment.objects.all()
    serializer_class = BusinessAdvertCommentSerializer


class ProviderAdvertCommentList(ListAPIView):
    queryset = ProviderAdvertComment.objects.all()
    serializer_class = ProviderAdvertCommentSerializer


class BusinessAdvertDetail(RetrieveAPIView):
    queryset = BusinessAdvert.objects.all()
    serializer_class = BusinessAdvertSerializer
    lookup_field = 'id'


class ProviderAdvertDetail(RetrieveAPIView):
    queryset = ProviderAdvert.objects.all()
    serializer_class = ProviderAdvertSerializer
    lookup_field = 'id'


def react_view(request):
    return render(request, 'index.html')