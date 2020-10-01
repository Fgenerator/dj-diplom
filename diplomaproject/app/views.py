from django.shortcuts import render


def index_view(request):
    template = 'index.html'
    context = {}

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
