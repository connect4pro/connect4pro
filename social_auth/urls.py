from django.urls import path

from .views import GoogleSocialAuthView, FacebookSocialAuthView

urlpatterns = [
    path('api/google/', GoogleSocialAuthView.as_view()),
    path('api/facebook/', FacebookSocialAuthView.as_view()),
]