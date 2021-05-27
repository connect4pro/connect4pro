from django.shortcuts import render
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from .models import Author, Category, Post
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, CreateAPIView
from forum.serializers import AuthorSerializer, CategorySerializer, PostSerializer
# Create your views here.

class AuthorList(APIView):
    permission_classes = ()

    @swagger_auto_schema(responses = {200: AuthorSerializer(many = True)})
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many = True)
        return Response(serializer.data)

    def post(self, request):
        """Создание мероприятия"""
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorCreate(CreateAPIView):
    serializer_class = AuthorSerializer



class CategoryList(APIView):
    permission_classes = ()

    @swagger_auto_schema(responses = {200: CategorySerializer(many = True)})
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many = True)
        return Response(serializer.data)

    def post(self, request):
        """Создание категории"""
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryCreate(CreateAPIView):
    serializer_class = CategorySerializer





class PostList(APIView):
    permission_classes = ()

    @swagger_auto_schema(responses = {200: PostSerializer(many = True)})
    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostCreate(CreateAPIView):
    serializer_class = PostSerializer