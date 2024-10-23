from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import * 


# Create your views here.



def index(request):
    context = {}
    context['recipes'] = Recipes.objects.all()
    return render(request , "recipe/index.html" , context ) 

def add_page(request):
    if request.method == 'POST' :
        data = request.POST 
        title = data.get('title')
        description = data.get('description')
        recipe_img = request.FILES.get('recipe_img')

    # to store in our model
        Recipes.objects.create(
            title = title,
            description = description, 
            recipe_img = recipe_img ,
        )

        return redirect('/add_page/')
    

    queryset = Recipes.objects.all()
    context = {
        'recipes' : queryset,
    }

    return render(request , "recipe/add_page.html" , context)


def delete_recipe(request , id):
    queryset = Recipes.objects.get(id = id)
    queryset.delete()
    return redirect('/')
