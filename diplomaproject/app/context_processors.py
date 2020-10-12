from .cart import Cart
from .models import Category


def cart(request):
    return {'cart': Cart(request)}


def categories_context_processor(context):
    categories_query = Category.objects.all()
    subcategories_query = Category.objects.all()
    return {'categories': categories_query,
            'subcategories': subcategories_query}
