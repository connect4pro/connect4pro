# Generated by Django 3.2 on 2021-05-21 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_businessprofile_employers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connect4prouser',
            name='is_freemium',
        ),
    ]
