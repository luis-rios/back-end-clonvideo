from django.db import models


class Pelicula_pagada(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    category = models.CharField(max_length=200, blank=False, null=False)
    img = models.CharField(max_length=200, blank=False, null=False)
    duration = models.TimeField()
    language = models.CharField(max_length=200, blank=False, null=False)
    subtitles = models.CharField(max_length=200, blank=False, null=False)
    creationDate = models.DateField(auto_now=True)
    classification = models.IntegerField()
    link = models.CharField(max_length=200, blank=False, null=False)
    rent = models.IntegerField()
    buy = models.IntegerField()
    direction = models.CharField(max_length=100, blank=False, null=False)
    distribution = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name