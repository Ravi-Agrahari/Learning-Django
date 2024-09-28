from django.urls import path 
from . import views 

urlpatterns = [
    path('' , views.foods_home , name='foods_home'),
    path('fruits/' , views.fruits , name='fruits'),
    path('fruits/<int:fruit_id>/' , views.fruit_detail , name='fruit_detail')
    
]
