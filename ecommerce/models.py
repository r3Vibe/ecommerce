from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='category/')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(to=Category)
    slug = models.SlugField()
    description = models.TextField(max_length=255)
    short_description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class VariationTypes(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class VariationValues(models.Model):
    name = models.CharField(max_length=255)
    VariationType = models.ForeignKey(
        to=VariationTypes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Variation(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    variation_type = models.ForeignKey(
        to=VariationTypes, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.product.title

    def __repr__(self):
        return self.product.title
