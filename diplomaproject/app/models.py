from django.db import models
from ckeditor.fields import RichTextField


class Product(models.Model):
    subcategory = models.ForeignKey('Subcategory',
                                    related_name='products',
                                    default=None,
                                    null=True,
                                    on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, default=None)
    image = models.ImageField(upload_to='products',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True, default=None)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True, default=None)
    parent = models.ForeignKey(Category,
                               related_name='child',
                               default=None,
                               on_delete=models.PROTECT)

    class Meta:
        ordering = ('name',)
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=50)
    header = models.CharField(max_length=100)
    text = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product,
                                      related_name='products',
                                      default=None)
    main_page = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
