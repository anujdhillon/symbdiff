# Generated by Django 3.0.3 on 2021-04-20 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.AddField(
            model_name='task',
            name='author',
            field=models.CharField(default='anonymous', max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
