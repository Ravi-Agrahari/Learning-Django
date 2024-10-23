from django.urls import path
from . import views

urlpatterns = [
    path("",views.index , name = "index"),
    path("delete-recipe/<id>" , views.delete_recipe , name="delete_recipe"),
    path("add_page/", views.add_page , name="add_page")
]
