# Generated by Django 3.0.2 on 2020-02-08 06:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='end_time',
        ),
        migrations.AddField(
            model_name='session',
            name='session_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 8, 8, 29, 3, 320068)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='session',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
