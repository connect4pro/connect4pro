from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from newsletter.models import Contacts
from newsletter.serializers import ContactsSerializer


class NewsletterSubscribe(CreateAPIView):
    serializer_class = ContactsSerializer
