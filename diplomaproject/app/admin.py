
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Product, Review, Category, Subcategory


class CategoryInline(admin.TabularInline):
    model = Subcategory
    fk_name = 'parent'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'slug', 'price',
                    'available',)
    list_filter = ('available', 'subcategory',)
    list_editable = ('price', 'available',)
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}

    inlines = [CategoryInline]


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent')
    prepopulated_fields = {'slug': ('name',)}


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_products', 'header', 'created', 'updated', 'main_page')
    list_filter = ('created', 'updated',)
    list_editable = ('main_page',)

    def get_products(self, obj):
        return ", ".join([product.name for product in obj.products.all()])

    get_products.short_description = 'Products'  # Renames column head


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
