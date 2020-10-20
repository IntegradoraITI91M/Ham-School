from django.db import models

# Create your models here.

class alumno(models.Model):
    apellidoP = models.CharField(max_length=35)
    apellidoM = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    sexos = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=sexos, default='M')
    edad = models.c

    def Nombrecompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.apellidoP, self.apellidoM, self.nombre)

    def __str__(self):
        return self.Nombrecompleto()

class curso(models.Model):
    Nombre = models.CharField(max_length=35)
    estado = models.BooleanField(default=True)

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.Nombre)

class Grado(models.Model):
    alumno = models.ForeignKey(alumno, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(curso, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        cadena = "{0} {1}"
        return cadena.format(self.alumno, self.curso)

        #hola mundo

        
