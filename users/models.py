from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

TURNOVER_CHOICES = ()


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active=True
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()
        return user


class Connect4ProUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    company_name = models.CharField(blank=True, max_length=100)
    phone = PhoneNumberField(blank=True)
    facebook = models.CharField(max_length=50,blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    site = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.email


class SectorChoices(models.Model):
    description = models.CharField(max_length=300)


class BusinessProfile(models.Model):
    user = models.OneToOneField(Connect4ProUser, on_delete=models.CASCADE, related_name='business_profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    turnover = models.CharField(choices=TURNOVER_CHOICES, max_length=20)
    employers = models.PositiveSmallIntegerField()
    sector = models.ManyToManyField(SectorChoices)
    demand = models.CharField(max_length=50, blank=True)
    supply = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.email


class ProviderProfile(models.Model):
    user = models.OneToOneField(Connect4ProUser, on_delete=models.CASCADE, related_name='provider_profile')
    manager = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    year = models.DateField()
    logo = models.ImageField(upload_to='images/provider/logo/%d%m%Y/')
    address = models.CharField(max_length=200, blank=True, null=True)
    services = models.CharField(max_length=200)
    scope = models.CharField(max_length=200)