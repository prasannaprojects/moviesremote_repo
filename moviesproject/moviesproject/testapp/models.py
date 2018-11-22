from django.db import models


# Create your models here.
class Movie(models.Model):
    rdate=models.DateField()
    moviename=models.CharField(max_length=124)
    hero=models.CharField(max_length=30)
    heroine=models.CharField(max_length=30)
    rating=models.IntegerField()
