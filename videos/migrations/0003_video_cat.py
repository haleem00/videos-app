# Generated by Django 3.2.4 on 2021-06-26 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='videos.cat'),
        ),
    ]