# Generated by Django 4.0.6 on 2022-08-18 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_remove_fotografia_ruta_fotografia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='fotografia',
            field=models.ImageField(blank=True, null=True, upload_to='frontend/static/photos'),
        ),
    ]