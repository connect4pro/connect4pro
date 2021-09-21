import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connect4pro.settings')
app = Celery('connect4pro')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'newsletter.tasks.send_newsletter',
        'schedule': crontab(minute='25', hour='23', day_of_week='3,5'),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
    'check_premium_every_day': {
        'task': 'payments.tasks.check_and_off_premium',
        'schedule': crontab(minute='0', hour='23'),
    },
}