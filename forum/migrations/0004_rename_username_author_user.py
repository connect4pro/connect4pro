# Generated by Django 3.2.3 on 2021-06-01 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_rename_user_author_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='username',
            new_name='user',
        ),
    ]
