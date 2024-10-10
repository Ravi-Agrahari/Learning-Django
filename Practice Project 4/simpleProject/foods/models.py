from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.
class fruits_data(models.Model):
    fruit_name = models.CharField(max_length=50)
    fruit_image = models.ImageField(upload_to='images/')
    fruit_description = models.TextField()
    calories = models.IntegerField() 


    def __str__(self):
        return self.fruit_name



#One to Many relationship
# let's create a model for the fruit reviews
# one fruit can have many reviews but one review can only belong to one fruit right ????

class fruitReview(models.Model):
    fruit = models.ForeignKey(fruits_data , on_delete=models.CASCADE , related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f"{self.user.username} review for {self.fruits_data.name}" 
    

# Many to many ...
# let's create a model for the fruit store 
# one fruit can be in many stores and one store can have many fruits right ???? , 

class store(models.Model):
    store_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    fruits = models.ManyToManyField(fruits_data, related_name="Stores")



    def __str__(self):
        return self.store_name
    

# one to one fields
# let's create a model for the fruit nutrition facts
# one fruit can have only one nutrition facts and one nutrition facts can only belong to one fruit right ????

class nutrition_facts(models.Model):
    fruit = models.OneToOneField(fruits_data, on_delete=models.CASCADE  , related_name='nutrition_facts')
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    fiber = models.FloatField()
    sugar = models.FloatField()
    cholesterol = models.FloatField()
    sodium = models.FloatField()
    potassium = models.FloatField()
    vitamin_a = models.FloatField()
    vitamin_c = models.FloatField()
    calcium = models.FloatField()
    iron = models.FloatField()

    def __str__(self):
        return f"nutrition facts for {self.fruit.fruit_name}"



 
    






