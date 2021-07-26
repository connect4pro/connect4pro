import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connect4pro.settings')
app = Celery('connect4pro')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'newsletter.tasks.send_newsletter',
        'schedule': crontab(minute='25', day_of_week='3,5'),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}