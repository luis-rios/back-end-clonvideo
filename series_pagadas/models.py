from django.db import models

from categorias.models import Categoria


class Serie_pagada(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    img = models.CharField(max_length=200, blank=False, null=False)
    seasons = models.IntegerField()
    rent = models.IntegerField()
    buy = models.IntegerField()
    languages = models.CharField(max_length=200, blank=False, null=False)
    subtitles = models.CharField(max_length=200, blank=False, null=False)
    creationDate = models.DateTimeField()
    classification = models.IntegerField()
    link = models.CharField(max_length=200, blank=False, null=False)
    category = models.CharField(max_length=200, blank=False, null=False)
    distribution = models.CharField(max_length=200, blank=False, null=False)
    direction = models.CharField(max_length=200, blank=False, null=False)

    categories = models.ManyToManyField(Categoria, related_name="Serie_pagada")

    def __str__(self):
        return self.name
