from django.shortcuts import render

# Create your views here.
def carts(request): 
    context = {
        'title': 'Home - Корзина',
    }
    return render(request, 'carts/carts.html', context)