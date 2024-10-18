from django.db import models


# Create your models here.
class Friends(models.Model):
    name  = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()
    
class Cars(models.Model):
    name = models.CharField(max_length=50)
    speed = models.IntegerField()

 