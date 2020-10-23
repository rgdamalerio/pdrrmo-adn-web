from django.contrib.gis.db import models

# Create your models here.


class Magallenes(models.Model):

    name = models.CharField(max_length=256, null=True)
    datetime = models.CharField(max_length=256, null=True)
    kindinfra = models.CharField(max_length=256, null=True)
    path = models.CharField(max_length=256, null=True)
    point = models.PointField()

    def __str__(self):
        return self.name
