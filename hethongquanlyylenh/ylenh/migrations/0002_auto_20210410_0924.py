# Generated by Django 3.2 on 2021-04-10 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ylenh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YLenh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('patient', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('day_start', models.DateTimeField(auto_now_add=True)),
                ('day_end', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]