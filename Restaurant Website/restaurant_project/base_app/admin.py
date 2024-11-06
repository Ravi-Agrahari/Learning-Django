from django.contrib import admin
from . import models 

# Register your models here.
admin.site.register(models.ItemList)
admin.site.register(models.Items)
admin.site.register(models.AboutUs)
admin.site.register(models.Feedbacks)
admin.site.register(models.BookTable)
