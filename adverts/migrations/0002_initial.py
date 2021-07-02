# Generated by Django 3.2 on 2021-07-02 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('adverts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provideradvert',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider_profile', to='users.providerprofile', verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='image',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='adverts.album'),
        ),
        migrations.AddField(
            model_name='businessadvert',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_advert_category', to='adverts.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='businessadvert',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_profile', to='users.businessprofile', verbose_name='Пользователь'),
        ),
    ]
