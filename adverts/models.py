from django.db import models
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField

from users.models import ProviderProfile, BusinessProfile

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

    name = models.CharField(max_length=60)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class BusinessAdvert(models.Model):
    """Объявление от МСБ"""
    #TODO:  связать с пользователем
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='business_advert_category')
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=9, default=0)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=usd, blank=True)
    completed = models.CharField(max_length=8, choices=COMPLETE_CHOICES, default=no)
    user = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE, related_name='business_profile')


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Объявление МСБ'
        verbose_name_plural = 'Объявления МСБ'


class ProviderAdvert(models.Model):
    """Объявление от провайдера\консультанта"""

    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='provider_profile')
    image_1 = ResizedImageField(size=[350, 250], upload_to=f'images/blog_images/%d%m%Y', blank=True,
                                   null=True)
    image_2 = ResizedImageField(size=[350, 250], upload_to=f'images/blog_images/%d%m%Y', blank=True,
                                null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='provider_advert_category')
    price = models.DecimalField(decimal_places=2, max_digits=9, default=0)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=usd, blank=True)



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление провайдера'
        verbose_name_plural = 'Объявления провайдеров'