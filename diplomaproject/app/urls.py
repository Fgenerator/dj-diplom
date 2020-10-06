from django.urls import path
from django.conf.urls import url
from app.views import index_view, product_view, category_view, login_view, cart_view, empty_section_view

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

app_name = 'app'

urlpatterns = [
    path('', index_view),
    path('product/<product_slug>', product_view),
    path('categories/<category_slug>/', category_view),
    path('login/', login_view),
    path('cart/', cart_view),
    path('empty_section/', empty_section_view),
    path('login/',  auth_views.LoginView.as_view(), {'template_name': 'login.html'},
         name='app_login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)