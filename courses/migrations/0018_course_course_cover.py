# Generated by Django 3.0.2 on 2020-02-10 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_remove_session_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_cover',
            field=models.ImageField(blank=True, upload_to='profile'),
        ),
    ]
