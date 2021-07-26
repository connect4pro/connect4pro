from django.urls import path

from newsletter.views import NewsletterSubscribe
app_name = 'newsletter'
urlpatterns = [
    path('api/subscribe/', NewsletterSubscribe.as_view(), name='newsletter_subscribe'),
]