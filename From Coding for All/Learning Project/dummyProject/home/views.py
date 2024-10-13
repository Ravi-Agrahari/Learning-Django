from django.shortcuts import render
from django.http import HttpResponse

# data ... 
peoples = [
    {'name':'Bishal', 'age':18 , 'address' : 'Nadawa' ,"phone_no" : "9817551210"},
    {'name':'Rithiga', 'age':19 , 'address' : 'TamilNadu' ,"phone_no" : "9817551210"},
    {'name':'Rikesh', 'age': 25, 'address' : 'Janakpur',"phone_no" : "9817551210"},
    {'name':'Kritika', 'age': 21, 'address' : 'Kathmandu',"phone_no" : "9817551210"},
    {'name':'Awadesh', 'age': 22, 'address' : 'lankahawa',"phone_no" : "9817551210"}
]

# Create your views here.
def home(request):
    # return HttpResponse("This is the homepage of dummyProject") ; 
   
    return render(request , "index.html" , context= {'peoples':peoples})


def contact(request):
    context = {
        'page': 'contact page' , 
        'peoples': peoples 
        }
    return render(request , "contact.html" ,context ) 


def about(request):
    context = {
        'page': 'about page', 
        'peoples': peoples 
        }
    return render(request , "about.html" ,context ) 


