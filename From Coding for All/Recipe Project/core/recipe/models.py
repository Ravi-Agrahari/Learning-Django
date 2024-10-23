from django.db import models

# Create your models here.
class Recipes(models.Model):
    title = models.CharField(max_length=200 )
    description = models.TextField()
    recipe_img = models.ImageField(upload_to="images/" )


    def __str__(self):
        return self.title
