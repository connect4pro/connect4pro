# Generated by Django 3.2.3 on 2021-05-28 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20210527_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='description'),
        ),
    ]
