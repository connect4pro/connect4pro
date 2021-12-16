from rest_framework import serializers

from links.models import TelegramLinks


class TelegramLinksSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.category')
    class Meta:
        model = TelegramLinks
        fields = ('category', 'ru_link', 'kg_link')