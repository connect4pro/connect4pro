from django.db import models

usd = 'USD'
som = 'Сом'

CURRENCY_CHOICES = (
    (usd, 'USD'),
    (som, 'Сом'),
)

yes = 'Да'
no = 'Нет'
left = 'Оставить'
COMPLETE_CHOICES = (
    (yes, 'Да'),
    (no, 'Нет'),
    (left, 'Оставить')
)


class Category(models.Model):
    """Категория объявления"""

    name = models.CharField(max_length=60, verbose_name = 'Название категории')
    description = models.CharField(max_length=300, verbose_name = 'Описание категории')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class UserAdvert(models.Model):
    """Объявление от пользователя"""

    name = models.CharField(max_length=200, verbose_name = 'Название объявления')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='advert_category', verbose_name = 'Категория объявления')
    description = models.TextField(verbose_name = 'Описание объявления')
    price = models.DecimalField(decimal_places=1, max_digits=9, default=0, verbose_name = 'Цена')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=usd, blank=True, verbose_name = 'Валюта')
    completed = models.CharField(max_length=8, choices=COMPLETE_CHOICES, default=no, verbose_name = 'Актуальность объявления')
    skills = models.TextField(blank=True, verbose_name = 'Умения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Объявление от пользователя'
        verbose_name_plural = 'Объявления от пользователей'
