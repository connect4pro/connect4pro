# Generated by Django 3.2 on 2021-05-16 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210516_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providerprofile',
            name='year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
