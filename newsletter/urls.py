from django.urls import path

from newsletter.views import NewsletterSubscribe, NewsletterUnsubscribe

app_name = 'newsletter'
urlpatterns = [
    path('api/subscribe/', NewsletterSubscribe.as_view(), name='newsletter_subscribe'),
    path('api/unsubscribe/', NewsletterUnsubscribe.as_view(), name='newsletter_unsubscribe'),
]