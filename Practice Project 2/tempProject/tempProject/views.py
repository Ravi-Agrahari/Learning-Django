from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("<h1> Hello This is Home page <h1> ")
    return render(request, 'website/index.html')