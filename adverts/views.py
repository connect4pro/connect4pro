from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from adverts.models import Category, UserAdvert, BlogPost
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




class BlogPostList(APIView):
    """
    Записи в блоге
    """
    permission_classes = ()

    @swagger_auto_schema(responses={200: BlogPostSerializer(many=True)})
    def get(self, request):
        posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(posts, many=True)
        return Response(serializer.data)
