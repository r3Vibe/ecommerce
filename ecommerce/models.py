from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='category/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Product Categories'

    def get_url(self):
        return reverse('ecommerce:product_by_category', args=[self.slug])

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
    has_variation = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class GallaryImages(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Gallary Image'
        verbose_name_plural = 'Product Gallary Images'

    def __str__(self):
        return self.product.title

    def __repr__(self):
        return self.product.title


class VariationCAtegory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Variation Category'
        verbose_name_plural = 'Product Variation Categories'


class Variations(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    variation_category = models.ForeignKey(
        to=VariationCAtegory, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.title}-{self.variation_category.name}-{self.value}"

    def __repr__(self):
        return f"{self.product.title}-{self.variation_category.name}-{self.value}"

    class Meta:
        verbose_name = 'Product Variation'
        verbose_name_plural = 'Product Variations'


class VariationCombinations(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(to=Variations)
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="products/")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Variation Combo'
        verbose_name_plural = 'Product Variation Combos'
