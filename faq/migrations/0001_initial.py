# Generated by Django 3.2 on 2021-07-12 17:46

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionsAndAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, verbose_name='Вопрос')),
                ('answer', models.CharField(max_length=255, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Вопрос - ответ',
                'verbose_name_plural': 'Вопросы и ответы',
            },
        ),
        migrations.CreateModel(
            name='WriteUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='Фамилия, имя, отчество')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Контактный номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Контактный адрес почты')),
                ('message', models.TextField(max_length=300, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Сообщение от пользователя',
                'verbose_name_plural': 'Сообщения от пользователей',
            },
        ),
    ]
