# Generated by Django 4.0.6 on 2022-08-19 14:45

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_alter_fotografia_fotografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='contenido',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
