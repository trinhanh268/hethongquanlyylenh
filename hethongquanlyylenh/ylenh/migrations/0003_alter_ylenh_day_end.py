# Generated by Django 3.2 on 2021-04-11 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ylenh', '0002_auto_20210410_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ylenh',
            name='day_end',
            field=models.DateField(),
        ),
    ]
