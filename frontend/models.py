# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from tinymce import models as tinymce_models

class Elemento(models.Model):
    id_elemento = models.AutoField(primary_key=True)
    ele_id_elemento = models.ForeignKey('self', models.DO_NOTHING, db_column='ele_id_elemento', blank=True, null=True)
    nombre = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'elemento'

    def __str__(self):
        return f'{self.id_elemento} - {self.nombre}'


class Ficha(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    id_elemento = models.ForeignKey(Elemento, models.DO_NOTHING, db_column='id_elemento', blank=True, null=True)
    contenido = tinymce_models.HTMLField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ficha'
    
    def __str__(self):
        backslash = '\n'
        return f'{self.id_elemento} - {str(self.contenido).split(backslash)[0]}'


class Fotografia(models.Model):
    id_fotografia = models.AutoField(primary_key=True)
    id_ficha = models.ForeignKey(Ficha, models.DO_NOTHING, db_column='id_ficha', blank=True, null=True)
    fotografia = models.ImageField(upload_to='frontend/static/photos', blank=True, null=True)
    nombre = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'fotografia'

    def __str__(self):
        return f'{self.id_fotografia} - {self.nombre}'
