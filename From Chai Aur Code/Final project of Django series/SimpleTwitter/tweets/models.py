'''
This file is used to define the models for the tweets app.
and the models are used to define the structure of the database tables.

The models are defined as classes in Django.
Each class represents a table in the database.
Each attribute of the class represents a column in the table.



'''


from django.db import models
# to use the User model from django.contrib.auth.models
from django.contrib.auth.models import User

# Create your models here.

'''
    Decription of the Tweet model:
        -> The Tweet model is used to store the tweets of the users.




'''


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=280)
    img = models.ImageField(upload_to='tweet_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return f'{self.user.username} tweeted: {self.text[:20]}'
