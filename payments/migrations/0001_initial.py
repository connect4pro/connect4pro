# Generated by Django 3.2 on 2021-09-01 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pg_payment_id', models.IntegerField(blank=True, null=True, verbose_name='Id PayBox')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='Сумма')),
                ('description', models.CharField(max_length=250, verbose_name='Описание')),
                ('status', models.CharField(choices=[('1', 'В процессе'), ('2', 'Оплачен'), ('3', 'Отменен')], default='1', max_length=8, verbose_name='Статус')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.customer', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Оплата премиум-аккаунта',
                'verbose_name_plural': 'Оплаты премиум-аккаунта',
            },
        ),
    ]
