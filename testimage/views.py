from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView

from testimage.models import Image
from testimage.serializers import ImageSerializer


class ImageView(CreateAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()