from django.db import models
from categorias.models import Categoria


class Espacio(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    Category = models.ManyToManyField(Categoria, related_name="Espacio")

    def __str__(self):
        return self.name
