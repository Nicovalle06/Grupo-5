# Generated by Django 3.0 on 2020-09-26 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0004_remove_comentario_comentario_aprobado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comentario',
        ),
    ]