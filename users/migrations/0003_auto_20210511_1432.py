# Generated by Django 3.2 on 2021-05-11 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210511_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='connect4prouser',
            name='is_freemium',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='connect4prouser',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]
