from django.urls import path

from newsletter.views import NewsletterSubscribe, NewsletterUnsubscribe, NewsletterList

app_name = 'newsletter'
urlpatterns = [
    path('api/subscribe/', NewsletterSubscribe.as_view(), name='newsletter_subscribe'),
    path('api/unsubscribe/<email>', NewsletterUnsubscribe.as_view(), name='newsletter_unsubscribe'),
    path('api/newsletter_list/', NewsletterList.as_view(), name='newsletter_list'),
]