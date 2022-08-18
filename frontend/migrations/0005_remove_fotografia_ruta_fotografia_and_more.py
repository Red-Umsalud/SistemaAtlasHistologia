# Generated by Django 4.0.6 on 2022-08-18 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_remove_ficha_numero_remove_ficha_titulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotografia',
            name='ruta_fotografia',
        ),
        migrations.AddField(
            model_name='fotografia',
            name='fotografia',
            field=models.ImageField(blank=True, null=True, upload_to='static/photos'),
        ),
    ]
