from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1> This is home page </h1>")
    return render(request , "website/home.html")

def about(request):
    return HttpResponse("<h1> This is about page </h1>")

