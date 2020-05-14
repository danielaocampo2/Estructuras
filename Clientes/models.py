from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    numero_contacto=models.IntegerField()
    email=models.EmailField()
    cumpleanos=models.DateField()
    contrasena=models.CharField(max_length=30)