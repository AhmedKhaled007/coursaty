# Generated by Django 3.0.2 on 2020-02-11 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0008_auto_20200210_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 9, 8, 7, 541930)),
        ),
    ]
