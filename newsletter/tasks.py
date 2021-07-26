from celery import shared_task
from django.core.mail import send_mass_mail, send_mail
from django.template.loader import render_to_string

from adverts.models import ProviderAdvert, BusinessAdvert
from connect4pro.celery import app
from events.models import Event
from grants_and_investments.models import Grant, Investment
from newsletter.models import Contacts


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


@shared_task
def send_newsletter():
    emails = Contacts.objects.values_list('email', flat=True)
    email_template = get_template()
    subject = 'Рассылка от connect4pro'
    message = (subject, email_template, 'connect4pro@google.com', emails)
    send_mass_mail([message], fail_silently=False)




