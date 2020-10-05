
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Product, Review, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'price',
                    'available',)
    list_filter = ('available', 'category',)
    list_editable = ('price', 'available',)
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_root', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_products', 'header', 'text', 'created', 'updated',)
    list_filter = ('created', 'updated',)
    list_editable = ('header', 'text',)

    def get_products(self, obj):
        return ", ".join([product.name for product in obj.products.all()])

    get_products.short_description = 'Products'  # Renames column head


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewsAdmin)
admin.site.register(Category, CategoryAdmin)