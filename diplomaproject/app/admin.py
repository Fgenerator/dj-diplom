
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Product, Reviews, Category, ProductCategoryInfo


class ProductInfoInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            #raise ValidationError('Тут всегда ошибка')
            raise ValidationError()
        return super().clean()  # вызываем базовый код переопределяемого метода


class ProductInfoInLine(admin.TabularInline):
    model = ProductCategoryInfo
    formset = ProductInfoInlineFormset


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image',)
    inlines = [
        ProductInfoInLine,
    ]


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'product',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_root',)


class ProductCategoryInfoAdmin(admin.ModelAdmin):
    list_display = ('product', 'category',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductCategoryInfo, ProductCategoryInfoAdmin)