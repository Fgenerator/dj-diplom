from django.urls import path
from app.views import index_view, product_view, category_view, cart_view, empty_section_view, signup_view

from django.contrib.auth import views as auth_views

app_name = 'app'

urlpatterns = [
    path('', index_view),
    path('product/<product_slug>', product_view),
    path('categories/<category_slug>/', category_view),
    path('cart/', cart_view),
    path('empty_section/', empty_section_view),
    path('signup/', signup_view, name='signup'),
    path(r'login/',  auth_views.LoginView.as_view(), {'template_name': 'registration/login.html'},
         name='app_login'),
    path('logout/',  auth_views.LogoutView.as_view(), {'template_name': 'index.html'}),
]


