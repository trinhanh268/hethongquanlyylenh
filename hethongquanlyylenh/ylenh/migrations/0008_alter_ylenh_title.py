# Generated by Django 3.2 on 2021-04-21 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ylenh', '0007_auto_20210421_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ylenh',
            name='title',
            field=models.CharField(default='Y Lenh', max_length=40),
        ),
    ]
