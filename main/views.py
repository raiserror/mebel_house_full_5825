from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# Create your views here.
def index(request):
    
    categories = Categories.objects.all()
    
    context = {
        'title': 'Home - Главная',
        'content': 'Главная страница магазина - Mebel House',
        'categories': categories
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'Mebel House - О нас',
    }
    return render(request, 'main/about.html', context)