from rest_framework import serializers

from testimage.models import TestImage


class TestImageSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = TestImage
        fields = '__all__'

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        image = None
        for image_data in images_data.values():
            image = TestImage.objects.create(image=image_data)
            image.save()
        return image