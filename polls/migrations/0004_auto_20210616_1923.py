# Generated by Django 3.2.3 on 2021-06-16 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_resultpoll_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultpoll',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='resultpoll',
            name='questions',
        ),
        migrations.AddField(
            model_name='answer',
            name='poll_result',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='polls.resultpoll'),
            preserve_default=False,
        ),
    ]