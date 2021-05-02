# Generated by Django 3.2 on 2021-04-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ylenh', '0008_alter_ylenh_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='ylenh',
            name='status',
            field=models.CharField(choices=[('C', 'Complete'), ('F', 'Fail'), ('D', 'Doing')], default='Doing', max_length=12),
        ),
    ]
