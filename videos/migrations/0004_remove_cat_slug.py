# Generated by Django 3.2.4 on 2021-06-26 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_video_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='slug',
        ),
    ]
