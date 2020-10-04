
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Product, Review, Category


class ProductReviewInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            #raise ValidationError('Тут всегда ошибка')
            #raise ValidationError()
        return super().clean()  # вызываем базовый код переопределяемого метода


class ProductReviewInLine(admin.TabularInline):
    model = Review
    formset = ProductReviewInlineFormset
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'price',
                    'available',)
    list_filter = ('available', 'category',)
    list_editable = ('price', 'available',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        ProductReviewInLine,
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_root', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'text', 'created', 'updated',)
    list_filter = ('created', 'updated',)
    list_editable = ('text',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewsAdmin)
admin.site.register(Category, CategoryAdmin)