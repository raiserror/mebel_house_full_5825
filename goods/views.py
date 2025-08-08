from django.shortcuts import render
from django.template import context
from .models import Categories
from goods.models import Products

# Create your views here.
def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)
    
    categories = Categories.objects.all()  
    
    # Проверяем, пустой ли список товаров
    is_empty = not goods.exists()
    
    context = {
        "categories": categories,
        "goods": goods,
        "is_empty": is_empty,  # Флаг для шаблона
    }
    
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    
    context = { 
        'product': product,
    }
    
    return render(request, 'goods/product.html', context=context)