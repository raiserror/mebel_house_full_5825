from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Главная страница магазина - Mebel House'
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'Mebel House - О нас',
    }
    return render(request, 'main/about.html', context)