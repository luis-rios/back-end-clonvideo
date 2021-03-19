from django.db import models

from espacios.models import Espacio


class Usuario(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    email = models.EmailField()
    password = models.CharField(max_length=100, blank=False, null=False)

    space = models.OneToOneField(Espacio, related_name="Usuario", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
