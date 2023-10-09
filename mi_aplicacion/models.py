
from django.db import models

class OfertaTrabajo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    def __str__(self):
        return self.titulo
# Create your models here.
