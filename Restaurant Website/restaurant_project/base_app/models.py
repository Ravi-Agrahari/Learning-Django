from django.db import models

# Create your models here.

class ItemList(models.Model):
    category_name = models.CharField(max_length=100)


class Items(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_description = models.TextField()
    item_image = models.ImageField(upload_to='images/')
    item_category = models.ForeignKey(ItemList, on_delete=models.CASCADE)


class AboutUs(models.Model):
    about_us_text = models.TextField()


class Feedbacks(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=100)
    user_feedback = models.TextField()
    rating = models.IntegerField()


class BookTable(models.Model):
    user_name = models.CharField(max_length=50)
    user_phonenumber = models.BigIntegerField()
    user_email = models.EmailField(max_length=50)
    number_of_guests = models.IntegerField()
    date = models.DateField()
