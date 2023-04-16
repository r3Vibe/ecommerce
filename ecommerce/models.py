from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='category/')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Product Categories'

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
    has_variation = models.BooleanField(default=True)
    price = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class Colours(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Colour'
        verbose_name_plural = 'Colours'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Sizes(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Variation(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    colour = models.ForeignKey(
        to=Colours, on_delete=models.CASCADE)
    size = models.ForeignKey(
        to=Sizes, on_delete=models.CASCADE)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Variation'
        verbose_name_plural = 'Product Variations'

    def __str__(self):
        return self.product.title

    def __repr__(self):
        return self.product.title


class GallaryImages(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    class Meta:
        verbose_name = 'Gallary Image'
        verbose_name_plural = 'Gallary Images'

    def __str__(self):
        return self.product.title

    def __repr__(self):
        return self.product.title
