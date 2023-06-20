from django.db import models

# Create your models here.

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_rol
    class Meta:
        db_table = "rol"

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)
    rol_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = "persona"

class Estudiante(models.Model):
    semestre = models.CharField(max_length=50)
    grupo = models.CharField(max_length=50)
    persona_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    class Meta:
        db_table = "estudiante"