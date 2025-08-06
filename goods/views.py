from django.shortcuts import render
from django.template import context

# Create your views here.
def catalog(request):
    context = {
        'title': 'Home - Каталог',
        'goods': [
         {'image': 'deps/images/goods/strange table.jpg',
         'name': 'Прикроватный столик',
         'description': 'Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.',
         'price': 55.00},

         {'image': 'deps/images/goods/office chair.jpg',
         'name': 'Стул офисный',
         'description': 'Стул идеален для квартиры типа Business...',
         'price': 90.00},

         {'image': 'deps/images/goods/set of tea table and two chairs.jpg',
         'name': 'Чайный столик и два стула',
         'description': 'Набор из стола и двух стульев в минималистическом стиле.',
         'price': 160.00},
         
         {'image': 'deps/images/goods/kitchen table.jpg',
         'name': 'Кухонный стол с раковиной',
         'description': 'Кухонный стол для обеда с встроенной раковиной и стульями.',
         'price': 450.00},

         {'image': 'deps/images/goods/flower.jpg',
         'name': 'Цветок стилизированный',
         'description': 'Дизайнерский цветок (возможно искусственный) для украшения интерьера.',
         'price': 30.00},

         {'image': 'deps/images/goods/double bed.jpg',
         'name': 'Двухспальная кровать',
         'description': 'Кровать двухспальная с надголовником, ортопедическая.',
         'price': 180.00},
        ]
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    return render(request, 'goods/product.html')