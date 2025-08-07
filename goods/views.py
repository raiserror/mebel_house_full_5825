from django.shortcuts import render
from django.template import context
from .models import Categories
from goods.models import Products

# Create your views here.
def catalog(request):
    categories = Categories.objects.all()  
    goods = Products.objects.all()
    context = {
        "categories": categories,
        "goods": goods,
    }
    
    return render(request, 'goods/catalog.html', context)

def product(request):
    return render(request, 'goods/product.html')