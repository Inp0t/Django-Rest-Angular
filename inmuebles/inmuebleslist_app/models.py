from django.db import models

class Inmueble(models.Model):
    direction = models.CharField(max_length=250)
    country = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=900)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.direction

