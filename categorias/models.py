from django.db import models

from peliculas.models import Pelicula
from peliculas_pagadas.models import Pelicula_pagada


class Categoria(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    movies = models.ManyToManyField(Pelicula, related_name="Categoria")
    paid_movies = models.ManyToManyField(Pelicula_pagada, related_name="Categoria")

    def __str__(self):
        return self.name
