from django.contrib import admin
from .models import Category, Product, Variation, Colours, Sizes, GallaryImages
import admin_thumbnails


class CategryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_display_links = ['name']
    list_editable = ['is_active']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (
            'Category Details',
            {
                "fields": ('name', 'slug',),
            }
        ),
        (
            'Status',
            {
                "fields": ('is_active',),
            }
        ),
    )


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1


@admin_thumbnails.thumbnail('image')
class GallaryInline(admin.TabularInline):
    model = GallaryImages
    extra = 1


@admin_thumbnails.thumbnail('image', 'preview')
class ProductAdmin(admin.ModelAdmin):
    list_display = ['image_thumbnail', 'title',
                    'short_description', 'price', 'has_variation', 'is_active']
    inlines = [VariationInline, GallaryInline]
    list_display_links = ['title']
    list_editable = ['is_active']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (
            'Product Details',
            {
                "fields": ('image_thumbnail', 'title', 'slug', 'description', 'short_description', 'category', 'image', 'has_variation', 'price'),
            }
        ),
    )


admin.site.register(Category, CategryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Colours)
admin.site.register(Sizes)
