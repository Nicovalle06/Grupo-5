# Generated by Django 3.0 on 2020-09-27 00:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myv', '0002_auto_20200926_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='verdad',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]