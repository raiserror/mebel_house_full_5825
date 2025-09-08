from goods.models import Categories

def first_category(request):
    try:
        return {'first_category': Categories.objects.first()}
    except:
        return {'first_category': None}