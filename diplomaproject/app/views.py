from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .cart import Cart
from .forms import SignUpForm, CartAddProductForm
from .models import Category, Product, Review, Subcategory

import urllib
from django.core.paginator import Paginator


def signup_view(request):
    template = 'registration/signup.html'
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
        'message': message,
    }

    return render(request, template, context)


def index_view(request):
    template = 'index.html'
    reviews = Review.objects.all()
    cart_product_form = CartAddProductForm()

    context = {
        'reviews': reviews,
        'cart_product_form': cart_product_form,
    }

    return render(request, template, context)


def product_view(request, product_id):
    template = 'product.html'
    current_product = get_object_or_404(Product, id=product_id)
    cart_product_form = CartAddProductForm()
    context = {
        'current_product': current_product,
        'cart_product_form': cart_product_form,
    }

    return render(request, template, context)


def category_view(request, category_slug):
    template = 'categories.html'

    cart_product_form = CartAddProductForm()

    current_category = get_object_or_404(Subcategory, slug=category_slug)
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
        'current_category': current_category,
        'cart_product_form': cart_product_form,
    })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', ' / '))


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('app:cart_detail')


def cart_detail(request):
    cart = Cart(request)

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True})

    context = {
        'cart': cart,
    }
    return render(request, 'cart.html', context)
