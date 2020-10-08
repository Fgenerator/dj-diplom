from django.urls import path
from app.views import index_view, product_view, category_view, empty_section_view, signup_view, logout_view, \
    cart_detail, cart_add, cart_remove

from django.contrib.auth import views as auth_views

app_name = 'app'

urlpatterns = [
    path('', index_view, name='home'),
    path('product/<product_id>', product_view),
    path('categories/<category_slug>/', category_view),
    #path('cart/', cart_view),
    path('empty_section/', empty_section_view),
    path('signup/', signup_view, name='signup'),
    path(r'login/',  auth_views.LoginView.as_view(), {'template_name': 'registration/login.html'},
         name='app_login'),
    path('logout/',  logout_view),
    path('cart/', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove,
         name='cart_remove'),
]



