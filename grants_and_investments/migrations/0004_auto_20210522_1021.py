# Generated by Django 3.2.3 on 2021-05-22 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants_and_investments', '0003_auto_20210522_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='grant_sum',
            field=models.PositiveIntegerField(verbose_name='Сумма гранта'),
        ),
        migrations.AlterField(
            model_name='investment',
            name='invest_sum',
            field=models.PositiveIntegerField(verbose_name='Сумма инвестиции'),
        ),
    ]
