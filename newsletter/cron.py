from django.core.mail import send_mass_mail, send_mail
from django.template.loader import render_to_string
from django_cron import CronJobBase, Schedule
from adverts.models import ProviderAdvert, BusinessAdvert
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


def send_newsletter():
    emails = Contacts.objects.values_list('email', flat=True)
    email_template = get_template()
    subject = 'Рассылка от connect4pro'
    send_mail(subject, email_template, 'connect4pro@google.com', emails, fail_silently=False)


class Newsletter(CronJobBase):
    RUN_EVERY_MINS = 1
    RUN_AT_TIMES = ['11:30', '14:00', '23:15']
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=0.5)
    code = 'newsletter.Newsletter'

    def do(self):
        send_newsletter()

