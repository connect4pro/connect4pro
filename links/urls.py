from django.urls import path

from links.views import LinksView

urlpatterns = [
    path('api/links', LinksView.as_view())
]