from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    direccion = models.CharField(max_length=255, blank=True, null=True, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True, unique=True)
    correo = models.EmailField(max_length=255, blank=True, null=True, unique=True)
    sitio_web = models.URLField(max_length=255, blank=True, null=True, unique=True)

    def __str__(self):
        return self.nombre

class Inscrito(models.Model):
    ESTADOS_CHOICES = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    nombre = models.CharField(max_length=255, unique=True)
    telefono = models.CharField(max_length=15,unique=True)
    fecha_inscripcion = models.DateField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    hora_inscripcion = models.TimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Project(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    instituciones = models.ManyToManyField('Institucion')

    def __str__(self):
        return self.nombre
