from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# Create your views here.
def index(request):
    
    categories = Categories.objects.all()
    
    context = {
        'title': 'Mebel House - Главная',
        'content': 'Главная страница магазина - Mebel House',
        'categories': categories,
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Mebel House - О нас',
        'content': 'Mebel House - О нас',
    }
    return render(request, 'main/about.html', context)

def contacts(request):
    context = {
        'title': 'Mebel House - Контакты',
        'content': 'Mebel House - Контакты',
    }
    return render(request, 'main/contacts.html', context)
