from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeView(request):
    return render(request, 'home_page.html')


def aboutView(request):
    return render(request, 'about_page.html')


def booktableView(request):
    return render(request, 'book_table_page.html')


def menuView(request):
    return render(request, 'menu_page.html')


def feedbackView(request):
    return HttpResponse("this is my feedback page")