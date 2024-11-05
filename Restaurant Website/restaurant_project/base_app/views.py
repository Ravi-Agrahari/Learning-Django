from django.shortcuts import render

# Create your views here.
def homeView(request):
    return render(request, 'home_page.html')


def aboutView(request):
    return render(request, 'about_page.html')


def booktableView(request):
    return render(request, 'book_table_page.html')


def menuView(request):
    return render(request, 'menu_page.html')