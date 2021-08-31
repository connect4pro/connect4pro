# Generated by Django 3.2 on 2021-08-31 17:20

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='СonsultationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ваше имя')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Ваш номер телефона')),
                ('messanger', models.CharField(max_length=30, verbose_name="Ваш Whats'App или Telegram")),
            ],
        ),
    ]
