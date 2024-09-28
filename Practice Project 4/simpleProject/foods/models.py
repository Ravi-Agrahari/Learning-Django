from django.db import models

# Create your models here.
class fruits_data(models.Model):
    fruit_name = models.CharField(max_length=50)
    fruit_image = models.ImageField(upload_to='images/')
    fruit_description = models.TextField()
    calories = models.IntegerField() 


    def __str__(self):
        return self.fruit_name


