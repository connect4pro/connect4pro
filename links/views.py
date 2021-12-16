from django.shortcuts import render
from rest_framework.generics import ListAPIView

from links.models import TelegramLinks
from links.serializers import TelegramLinksSerializer


class LinksView(ListAPIView):
    queryset = TelegramLinks.objects.all()
    serializer_class = TelegramLinksSerializer