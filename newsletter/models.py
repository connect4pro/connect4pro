from django.db import models

# Create your models here.

class Contacts(models.Model):
    """Адреса подписчиков на рассылку"""
    email = models.EmailField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Подписчик на рассылку'
        verbose_name_plural = 'Подписчики на рассылку'