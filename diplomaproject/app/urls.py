from django.urls import path

from app.views import index_view, product_view, category_view, login_view, cart_view, empty_section_view

from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'

urlpatterns = [
    path('', index_view),
    path('product/<product_slug>', product_view),
    path('categories/<category_slug>/', category_view),
    path('login/', login_view),
    path('cart/', cart_view),
    path('empty_section/', empty_section_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)