from django.http import HttpResponse 
from django.shortcuts import render


def home(request):
    # return HttpResponse("<h1> Hello Ravi , This is your home page </h1>")
    return render(request,'website/index.html')

def about(request):
    # return HttpResponse("<h1> This is your About page , SomeThing about you is here ...  </h1>")
    return render(request, 'website/about.html')

def contact(request):
    return HttpResponse("<h1> This is your Contact page , You can view your contacts </h1>")

def blogs(request):
    return HttpResponse("<h1>  This is your Blogs page , do bloging ...  </h1>")
