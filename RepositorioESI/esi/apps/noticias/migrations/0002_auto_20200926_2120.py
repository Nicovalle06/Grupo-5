# Generated by Django 3.0 on 2020-09-27 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='copete',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='new',
            name='fuente',
            field=models.CharField(default='', max_length=400),
        ),
    ]
