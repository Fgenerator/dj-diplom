from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    image = models.FileField(upload_to='products/%Y/%m/%d/')


class Reviews(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')


class Category(models.Model):
    name = models.CharField(max_length=50)
    products = models.ManyToManyField(
        Product,
        through='ProductCategoryInfo',
        default=None,
    )
    is_root = models.BooleanField(default=True)


class ProductCategoryInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
