# Generated by Django 3.2 on 2021-06-17 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businessprofile',
            options={'verbose_name': 'Профиль МСБ', 'verbose_name_plural': 'Профили МСБ'},
        ),
    ]