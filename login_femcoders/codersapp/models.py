from django.db import models

# Create your models here.
class Materia(models.Model):
    materias = models.CharField(max_length=25)
    comentarios = models.TextField(max_length=100)

    def __str__(self):
        return f' {self.materias}'


class Profesor(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=25)
    materia = models.ManyToManyField(Materia)

    def __str__(self):
        return f'Profesor {self.id}:{self.nombre}'


class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    fotoPerfil= models.FileField
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    dni = models.CharField(max_length=9)
    telefono = models.CharField(max_length=12)
    email = models.EmailField(max_length=25)
    fNacimiento = models.DateField()
    materia = models.ManyToManyField(Materia)

    def __str__(self):
        return f'Alumno {self.id}:{self.nombre}'


class Evaluacion(models.Model):
    materia = models.ForeignKey(Materia,on_delete=models.SET_NULL, null=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.SET_NULL, null=True)
    nota = models.FloatField(null=True, blank=True)
    comentario = models.TextField(max_length=100)

    def __str__(self):
        return f'Evaluacion {self.alumno} {self.materia} {self.nota} {self.comentario}'