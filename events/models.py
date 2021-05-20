from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class Event(models.Model):
    """Мероприятие (тема, дата, время, сумма (вход))"""
    name = models.CharField(max_length = 100)
    event_image = ResizedImageField(size=[250, 250], upload_to=f'images/events_images/{name}-%d%m%Y', blank=True,
                                   null=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length = 100)
    sum = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'