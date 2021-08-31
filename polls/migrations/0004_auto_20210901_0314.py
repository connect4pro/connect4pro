# Generated by Django 3.2 on 2021-08-31 21:14

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210901_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер телефона')),
                ('messanger', models.CharField(max_length=30, verbose_name="Whats'App или Telegram")),
            ],
            options={
                'verbose_name': 'Обращение через форму для консультации',
                'verbose_name_plural': 'Все обращения через форму для консультаций',
            },
        ),
        migrations.DeleteModel(
            name='СonsultationForm',
        ),
    ]
