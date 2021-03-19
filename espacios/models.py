from django.db import models
from categorias.models import Categoria
from peliculas.models import Pelicula
from peliculas_pagadas.models import Pelicula_pagada
from series.models import Serie
from series_pagadas.models import Serie_pagada


class Espacio(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    Category = models.ManyToManyField(Categoria, related_name="Espacio")

    series = models.ManyToManyField(Serie, related_name="Espacio")
    movie = models.ManyToManyField(Pelicula, related_name="Espacio")
    paid_series = models.ManyToManyField(Serie_pagada, related_name="Espacio")
    paid_movie = models.ManyToManyField(Pelicula_pagada, related_name="Espacio")

    def __str__(self):
        return self.name
