from django.contrib import admin
from .models import Category, Product, VariationTypes, VariationValues, Variation


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


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'is_active']
    list_display_links = ['title']
    list_editable = ['is_active']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (
            'Product Details',
            {
                "fields": ('title', 'slug', 'description', 'short_description', 'category', 'image'),
            }
        ),
    )


admin.site.register(Category, CategryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(VariationTypes)
admin.site.register(VariationValues)
admin.site.register(Variation)
