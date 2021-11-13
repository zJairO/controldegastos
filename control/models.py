from django.db import models

class Ingresos(models.Model):
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=50)
    monto = models.IntegerField()

    def __str__(self):
        return self.descripcion

class Egresos(models.Model):
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=50)
    monto = models.IntegerField()

    def __str__(self):
        return self.descripcion