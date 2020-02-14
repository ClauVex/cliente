from django.db import models
from django.utils import timezone

class CiudadModel(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.pk

    class Meta:
        db_table = 'Ciudad'

class GeneroModel(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.pk

    class Meta:
        db_table = 'Genero'
    

class OcupacionModel(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.pk

    class Meta:
        db_table = 'Ocupacion'

class EstadoModel(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.pk

    class Meta:
        db_table = 'Estado'

class EstCivModel(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.pk

    class Meta:
        db_table = 'Estado Civil'

class ProfileModel(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    apellido_P = models.CharField(max_length=254, null=False)
    apellido_M = models.CharField(max_length=254, null=False)
    edad = models.IntegerField(null=False)
    ciudad = models.ForeignKey(CiudadModel,on_delete=models.CASCADE)
    genero = models.ForeignKey(GeneroModel,on_delete=models.CASCADE)
    ocupacion = models.ForeignKey(OcupacionModel,on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoModel,on_delete=models.CASCADE)
    estado_Civ = models.ForeignKey(EstCivModel,on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.pk

    class Meta:
        db_table = 'Profile'


# Create your models here.
