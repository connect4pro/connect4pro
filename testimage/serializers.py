from rest_framework import serializers

from testimage.models import TestImage


class TestImageSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = TestImage
        fields = ('image',)

    def create(self, validated_data):
        images_data = self.context.get('file').request.FILES
        return TestImage.objects.create(**validated_data)