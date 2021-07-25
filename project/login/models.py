from django.db import models
from django.db.models.fields import CharField


class Movie(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=200, null=True)
    genre = models.CharField(max_length=200, null = True)
    release_date = models.DateField(null=True)


    def __str__(self) :
        return self.name


