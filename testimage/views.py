from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView

from testimage.models import TestImage
from testimage.serializers import TestImageSerializer


class ImageView(CreateAPIView):
    serializer_class = TestImageSerializer
    queryset = TestImage.objects.all()