# Generated by Django 3.2 on 2021-04-19 03:34

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ylenh', '0003_alter_ylenh_day_end'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ylenh',
            name='username',
        ),
        migrations.AddField(
            model_name='ylenh',
            name='username_id',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.contrib.auth.models.User, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ylenh',
            name='day_end',
            field=models.DateField(verbose_name='Day End(mm/dd/yyyy)'),
        ),
    ]
