from django.shortcuts import render, get_object_or_404, redirect

from .forms import SignUpForm
from .models import Category, Product, Review

import urllib
from django.core.paginator import Paginator


def signup_view(request):
    template = 'registration/signup.html'
    categories = Category.objects.all()
    message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = SignUpForm(request.POST)
            message = 'Введены некорректные данные'
    else:
        form = SignUpForm(request.POST)

    context = {
        'form': form,
        'categories': categories,
        'message': message,
    }

    return render(request, template, context)


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
    return render(request, template, context={
        'current_products': current_products,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
        'categories': categories,
        'current_category': current_category,
    })


def cart_view(request):
    template = 'cart.html'
    context = {}

    return render(request, template, context)


def empty_section_view(request):
    template = 'empty_section.html'
    context = {}

    return render(request, template, context)
