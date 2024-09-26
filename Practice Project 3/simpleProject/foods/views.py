from django.shortcuts import render
from .models import fruits_data 
from django.shortcuts import get_object_or_404


# Create your views here.
def foods_home(request):
    return render(request , "foods_home.html")

def fruits(request):
    fruits_datas = fruits_data.objects.all()
    return render(request , "fruits.html" , {'fruits_datas' : fruits_datas })

def fruit_detail(request, fruit_id):
    fruit = get_object_or_404(fruits_data, pk=fruit_id)
    return render(request , "fruit_detail.html" , { 'fruit' : fruit })





