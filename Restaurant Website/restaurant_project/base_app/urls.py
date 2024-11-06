from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.homeView, name="home"),
    path('menu/' , views.menuView , name="menu"),
    path('book_table/' ,views.booktableView , name="book_table"), 
    path('about/', views.aboutView , name="about"),
    path('feedback/', views.feedbackView , name="feedback")
]
