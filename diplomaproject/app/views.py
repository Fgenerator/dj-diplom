from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Review

import urllib
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import render_to_response, redirect


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


def product_view(request, product_slug):
    template = 'product.html'
    categories = Category.objects.all()
    current_product = get_object_or_404(Product, slug=product_slug)
    context = {
        'categories': categories,
        'current_product': current_product
    }

    return render(request, template, context)


def category_view(request, category_slug):
    template = 'categories.html'
    categories = Category.objects.all()

    current_category = get_object_or_404(Category, slug=category_slug)
    current_products = current_category.products.all()

    paginator = Paginator(current_products, 3)
    current_page = int(request.GET.get('page', 1))
    current_products = paginator.get_page(current_page)
    prev_page_url, next_page_url = None, None
    if current_products.has_previous():
        prev_page = current_products.previous_page_number()
        payload = urllib.parse.urlencode({'page': prev_page})
        prev_page_url = f'?{payload}'
    if current_products.has_next():
        next_page = current_products.next_page_number()
        payload = urllib.parse.urlencode({'page': next_page})
        next_page_url = f'?{payload}'
    return render_to_response(template, context={
        'current_products': current_products,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
        'categories': categories,
        'current_category': current_category,
    })


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
