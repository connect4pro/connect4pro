from django.shortcuts import render
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from newsletter.models import Contacts
from newsletter.serializers import ContactsSerializer


class NewsletterSubscribe(CreateAPIView):
    serializer_class = ContactsSerializer


class NewsletterUnsubscribe(DestroyAPIView):
    serializer_class = ContactsSerializer
    lookup_field = 'email'

    def get_queryset(self):
        queryset = Contacts.objects.first()
        return queryset
