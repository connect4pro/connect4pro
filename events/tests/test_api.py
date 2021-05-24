from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from adverts.models import Category, UserAdvert
from adverts.serializers import CategorySerializer, UserAdvertSerializer


class CategoryApiTestCase(APITestCase):
    def test_get(self):
        client = APIClient()
        category_1 = Category.objects.create(name='Test category', description='Test description')
        category_2 = Category.objects.create(name='Test category2', description='Test description2')
        url = reverse('category-list')
        response = client.get(url)
        serializer_data = CategorySerializer([category_1, category_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class UserAdvertApiTestCase(APITestCase):
    def test_get(self):
        client = APIClient()
        category_1 = Category.objects.create(name='Test category', description='Test description')
        advert_1 = UserAdvert.objects.create(name='Test advert', description='Test', category=category_1, price='20.0',
                                             currency='Som')
        advert_2 = UserAdvert.objects.create(name='Test advert', description='Test', category=category_1, price='20.0',
                                             currency='Som')
        url = reverse('useradverts')
        response = client.get(url)
        serializer_data = UserAdvertSerializer([advert_1, advert_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
