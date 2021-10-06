from rest_framework import serializers

from newsletter.models import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = Contacts
        fields = ('id', 'email',)
