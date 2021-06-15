from django.template.loader import render_to_string

from adverts.models import ProviderAdvert, BusinessAdvert
from events.models import Event
from grants_and_investments.models import Grant, Investment


def get_template():
    provider_adverts = ProviderAdvert.objects.all()[:5]
    business_adverts = BusinessAdvert.objects.all()[:5]
    events = Event.objects.all()[:5]
    grants = Grant.objects.all()[:5]
    investments = Investment.objects.all()[:5]
    context = {
        'provider_adverts': provider_adverts,
        'business_adverts': business_adverts,
        'events': events,
        'grants': grants,
        'investments': investments,
    }
    email_template = render_to_string('email/newsletter.html', context)
    return email_template
