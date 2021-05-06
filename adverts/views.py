from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from adverts.models import Category, UserAdvert
from adverts.serializers import CategorySerializer, UserAdvertSerializer


class CategoryList(APIView):
    """
    Список всех категорий.
    """
    permission_classes = ()

    @swagger_auto_schema(responses={200: CategorySerializer(many=True)})
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: CategorySerializer()})
    def post(self, request):
        """Создание категории"""
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAdvertList(APIView):
    """
    Список объявлений пользователя
    """
    permission_classes = ()

    @swagger_auto_schema(responses={200: UserAdvertSerializer(many=True)})
    def get(self, request):
        adverts = UserAdvert.objects.all()
        serializer = UserAdvertSerializer(adverts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: UserAdvertSerializer()})
    def post(self, request):
        """Создание объявления"""
        serializer = UserAdvertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
