# Generated by Django 3.2 on 2021-05-10 12:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ylenh', '0010_auto_20210502_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='ylenh',
            name='day_update',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
