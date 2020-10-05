from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Review


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'media': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})


def index_view(request):
    template = 'index.html'
    categories = Category.objects.all()
    reviews = Review.objects.all()

    context = {
        'categories': categories,
        'reviews': reviews,
    }

    return render(request, template, context)


def phone_view(request):
    template = 'phone.html'
    context = {}

    return render(request, template, context)


def smartphone_view(request):
    template = 'smartphones.html'
    context = {}

    return render(request, template, context)


def login_view(request):
    template = 'login.html'
    context = {}

    return render(request, template, context)


def cart_view(request):
    template = 'cart.html'
    context = {}

    return render(request, template, context)


def empty_section_view(request):
    template = 'empty_section.html'
    context = {}

    return render(request, template, context)
