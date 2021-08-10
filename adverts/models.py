from django.db import models
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField

from users.models import ProviderProfile, BusinessProfile, Connect4ProUser

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


class Album(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        verbose_name = 'Набор изображений'
        verbose_name_plural = 'Наборы изображений'


class Image(models.Model):
    image = ResizedImageField(size=[350, 250], upload_to=f'images/adverts/%d%m%Y', blank=True,
                              null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='images')


class Category(models.Model):
    """Категория объявления"""

    name = models.CharField(verbose_name='Категория', max_length=60)
    description = models.CharField(verbose_name='Описание', max_length=300)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class BusinessAdvert(models.Model):
    """Объявление от МСБ"""

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE,
                                 related_name='business_advert_category')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(decimal_places=2, verbose_name='Цена', max_digits=9, default=0)
    currency = models.CharField(max_length=3, verbose_name='Валюта', choices=CURRENCY_CHOICES, default=usd, blank=True)
    completed = models.CharField(max_length=8, verbose_name='Завершено', choices=COMPLETE_CHOICES, default=no)
    user = models.ForeignKey(BusinessProfile, verbose_name='Пользователь', on_delete=models.CASCADE,
                             related_name='business_profile')
    needs = models.CharField(max_length=1000, verbose_name='Мне нужно', blank=True, null=True)
    suggest = models.CharField(max_length=1000, verbose_name='Я предлагаю', blank=True, null=True)
    tel = models.CharField(max_length=20, verbose_name='Телефон', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Объявление МСБ'
        verbose_name_plural = 'Объявления МСБ'


class ProviderAdvert(models.Model):
    """Объявление от провайдера\консультанта"""

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    user = models.ForeignKey(ProviderProfile, verbose_name='Пользователь', on_delete=models.CASCADE,
                             related_name='provider_profile')
    images = models.ForeignKey(Album, verbose_name='Фото', on_delete=models.CASCADE, related_name='image_set')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE,
                                 related_name='provider_advert_category')
    price = models.DecimalField(decimal_places=2, verbose_name='Цена', max_digits=9, default=0)
    currency = models.CharField(max_length=3, verbose_name='Валюта', choices=CURRENCY_CHOICES, default=usd, blank=True)
    tel = models.CharField(max_length=20, verbose_name='Телефон', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление провайдера'
        verbose_name_plural = 'Объявления провайдеров'


class BusinessAdvertComment(models.Model):
    text = models.TextField(max_length=500, verbose_name='Ваш комментарий')
    user = models.ForeignKey(Connect4ProUser, on_delete=models.CASCADE, verbose_name='Пользователь',
                             related_name='business_commenter')
    post = models.ForeignKey(BusinessAdvert, verbose_name='Объявление', on_delete=models.CASCADE,
                             related_name='post_comment')
    posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Имя: {self.user.email}'



    class Meta:
        verbose_name = 'Комментарий объявления МСБ'
        verbose_name_plural = 'Комментарии объявлений МСБ'


class ProviderAdvertComment(models.Model):
    text = models.TextField(max_length=500, verbose_name='Ваш комментарий')
    user = models.ForeignKey(Connect4ProUser, on_delete=models.CASCADE, verbose_name='Пользователь',
                             related_name='provider_commenter')
    post = models.ForeignKey(ProviderAdvert, verbose_name='Объявление', on_delete=models.CASCADE,
                             related_name='post_comment')
    posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Имя: {self.user.email}'

    class Meta:
        verbose_name = 'Комментарий объявления консультанта'
        verbose_name_plural = 'Комментарии объявлений консультантов'
