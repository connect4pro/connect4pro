from rest_framework import serializers

from testimage.models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Image
        fields = '__all__'

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        image = None
        for image_data in images_data.values():
            image = Image.objects.create(image=image_data)
            image.save()
        return image