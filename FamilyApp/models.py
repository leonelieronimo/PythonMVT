from django.db import models
from django.forms import CharField
from django.db import models

# Create your models here.
class Familia(models.Model):
    nombreFamiliar = models.CharField(max_length=20)
    fechaNacimiento = models.DateField()
    edad = models.IntegerField()

