from django.shortcuts import render, HttpResponse

# Create your views here.

# functions to return the pages as per urls passed 

def index(request):
    info = {
        'name' : "Ravi Agrahari",
        'address' : "Ramgram-10, Nadawa, Nepal"
    }  
    return render(request , 'index.html' , info)
    # return HttpResponse("This is home page ")

def about(request):
    return HttpResponse('This is about page ... ')

def contact(request):
    return HttpResponse('This is contact page ... ')
