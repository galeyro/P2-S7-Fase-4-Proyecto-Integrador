from django.db import models

# Create your models here.

class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    lugar_nacimiento = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono_alumno = models.CharField(max_length=20, null=True, blank=True)
    info_escolar = models.CharField(max_length=255, null=True, blank=True)
    info_salud = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'Alumno'
        managed = False

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
