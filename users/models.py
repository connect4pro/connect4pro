from datetime import datetime, date

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, User
from django.core.mail import send_mail
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django_resized import ResizedImageField
from rest_framework_simplejwt.tokens import RefreshToken
from django_rest_passwordreset.signals import reset_password_token_created

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


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google', 'email': 'email'}


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'),
                                                   reset_password_token.key)

    send_mail(
        # title:
        'Сброс пароля',
        # message:
        email_plaintext_message,
        # from:
        "admin@connect4.pro",
        # to:
        [reset_password_token.user.email],
    )


class Connect4ProUser(AbstractUser):
    """Общая для всех основа пользователя"""

    # По умолчанию основное поле - email
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    first_name = models.CharField(verbose_name='Имя', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30, blank=True)
    birth_date = models.DateField(verbose_name='Дата рождения', null=True)
    gender = models.CharField(verbose_name='Пол', max_length=8, blank=True)
    country = models.CharField(verbose_name='Страна', max_length=25, blank=True)
    city = models.CharField(verbose_name='Город/Село', max_length=40, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=20, blank=True)
    telegram = models.CharField(verbose_name='Telegram', max_length=20, blank=True)
    site = models.CharField(verbose_name='Сайт/Соцсети', max_length=50, blank=True)
    avatar = ResizedImageField(size=[350, 350], upload_to='images/users/avatars/%d%m%Y', blank=True,
                               null=True, default='images/users/avatars/avatardefault_92824.png')
    is_premium = models.BooleanField(default=False, verbose_name='Премиум-статус')
    start_date = models.DateTimeField(verbose_name='Дата начала премиум', null=True, blank=True)
    end_date = models.DateTimeField(verbose_name='Дата окончания премиум', null=True, blank=True)
    is_business = models.BooleanField(default=False, verbose_name='Профиль МСБ')
    is_provider = models.BooleanField(default=False, verbose_name='Профиль провайдера')
    auth_provider = models.CharField(max_length=255, blank=False, null=False, default=AUTH_PROVIDERS.get('email'),
                                     verbose_name='Провайдер аутентификации')

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    def __str__(self):
        if self.is_premium and self.is_business:
            return f'{self.email} - Премиум - Бизнес'
        elif self.is_premium and self.is_provider:
            return f'{self.email} - Премиум - Провайдер'
        elif not self.is_premium and self.is_business:
            return f'{self.email} - Базовый - Бизнес'
        elif not self.is_premium and self.is_provider:
            return f'{self.email} - Базовый - Провайдер'
        else:
            return self.email


class Sector(models.Model):
    """Сектор деятельности"""
    name = models.CharField(verbose_name='Название', max_length=300, default='', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сектор деятельности'
        verbose_name_plural = 'Секторы деятельности'


class Knowledge(models.Model):
    """Знания"""
    name = models.CharField(verbose_name='Название', max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Знание'
        verbose_name_plural = 'Знания'


class Skill(models.Model):
    """Навыки"""
    name = models.CharField(verbose_name='Название', max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class Method(models.Model):
    """Методологии"""
    name = models.CharField(verbose_name='Название', max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Методология'
        verbose_name_plural = 'Методологии'


class BusinessProfile(models.Model):
    """Профиль пользователя МСБ"""

    user = models.OneToOneField(Connect4ProUser, verbose_name='Пользователь', on_delete=models.CASCADE,
                                related_name='business_profile')
    sector = models.ManyToManyField(Sector, verbose_name='Сектор деятельности', blank=True)
    turnover = models.CharField(verbose_name='Примерный оборот', max_length=20, blank=True)
    employers = models.PositiveSmallIntegerField(verbose_name='Число сотрудников', blank=True, default=1)
    category = models.CharField(verbose_name='Категориясотрудников', blank=True, max_length=60)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Профиль МСБ'
        verbose_name_plural = 'Профили МСБ'


class ProviderProfile(models.Model):
    """Профиль провайдера/консультанта"""

    user = models.OneToOneField(Connect4ProUser, verbose_name='Пользователь', on_delete=models.CASCADE,
                                related_name='provider_profile')
    skills = models.ManyToManyField(Skill, verbose_name='Навыки', blank=True, related_name='skills')
    knowledge = models.ManyToManyField(Knowledge, verbose_name='Знания', blank=True)
    methods = models.ManyToManyField(Method, verbose_name='Методологии', blank=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Профиль консультанта'
        verbose_name_plural = 'Профили консультантов'
