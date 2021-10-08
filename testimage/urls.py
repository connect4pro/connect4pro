from django.urls import path

from testimage.views import ImageView

urlpatterns = [
    path('api/image_create/', ImageView.as_view(), name='image_create'),
]