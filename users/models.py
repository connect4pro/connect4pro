from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken

from connect4pro import settings
from .choices import TURNOVER_CHOICES, REGION_CHOICES

# Поле email теперь уникально
User._meta.get_field('email')._unique = True


class CustomUserManager(BaseUserManager):
    """
    Кастомный менеджер модели пользователя, который заменяет дефолтный вход
    с username на email
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Создать и сохранить пользователя с введенным email и паролем
        """
        if not email:
            raise ValueError(_('Поле email обязательное'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save()

        return user

    def create_superuser(self, email, password):
        """создание суперпользователя"""
        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()
        return user


class Connect4ProUser(AbstractUser):
    """Общая для всех основа пользователя"""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    avatar = ResizedImageField(size=[350, 350], upload_to=f'images/users/avatars/%d%m%Y', blank=True,
                               null=True)

    company_name = models.CharField(verbose_name='Название компании', blank=True, max_length=100)
    phone = PhoneNumberField(verbose_name='Телефон/Telegram', blank=True)
    facebook = models.CharField(verbose_name='Facebook', max_length=50, blank=True)
    instagram = models.CharField(verbose_name='Instagram', max_length=50, blank=True)
    site = models.CharField(verbose_name='Сайт', max_length=50, blank=True)
    is_premium = models.BooleanField(default=False, verbose_name='Премиум-статус')
    start_date = models.DateTimeField(verbose_name='Дата начала премиум',null=True)
    end_date = models.DateTimeField(verbose_name='Дата окончания премиум', null=True)

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    def __str__(self):
        return self.email


class Sector(models.Model):
    """Сектор деятельности"""
    description = models.CharField(verbose_name='Описание', max_length=300)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Сектор деятельности'
        verbose_name_plural = 'Секторы деятельности'


class BusinessProfile(models.Model):
    """Профиль пользователя МСБ"""

    user = models.OneToOneField(Connect4ProUser, verbose_name='Пользователь', on_delete=models.CASCADE,
                                related_name='business_profile')
    first_name = models.CharField(verbose_name='Имя', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30, blank=True)
    region = models.CharField(choices=REGION_CHOICES, verbose_name='Регион', max_length=30, default=1)
    turnover = models.CharField(choices=TURNOVER_CHOICES, verbose_name='Примерный оборот', max_length=20, default=1)
    employers = models.PositiveSmallIntegerField(verbose_name='Число сотрудников', blank=True, default=1)
    sector = models.ManyToManyField(Sector, verbose_name='Сектор деятельности', blank=True)
    demand = models.CharField(verbose_name='Ищу', max_length=50, blank=True)
    supply = models.CharField(verbose_name='Предлагаю', max_length=50, blank=True)
    as_business = models.BooleanField(default=True, verbose_name='Профиль МСБ')

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Профиль МСБ'
        verbose_name_plural = 'Профили МСБ'


class ProviderProfile(models.Model):
    """Профиль провайдера/консультанта"""

    user = models.OneToOneField(Connect4ProUser, on_delete=models.CASCADE, related_name='provider_profile')
    manager = models.CharField(verbose_name='ФИО руководителя', max_length=100, blank=True)
    description = models.CharField(verbose_name='Описание', max_length=300, blank=True)
    year = models.DateField(verbose_name='Год основания', blank=True, null=True)
    logo = models.ImageField(verbose_name='Логотип', upload_to='images/provider/logo/%d%m%Y/', blank=True, null=True)
    address = models.CharField(verbose_name='Адрес', max_length=200, blank=True, default='')
    services = models.CharField(verbose_name='Список услуг', max_length=200, blank=True)
    scope = models.CharField(verbose_name='Сфера деятельности', max_length=200, blank=True)
    as_provider = models.BooleanField(default=True, verbose_name='Профиль консультанта')

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Профиль консультанта'
        verbose_name_plural = 'Профили консультантов'
