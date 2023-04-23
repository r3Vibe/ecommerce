from django.shortcuts import render
from .models import VariationCAtegory, Variations, VariationCombinations
from django.db.models import Q


def store_view(req, category_slug=None):
    if category_slug is not None:
        products = VariationCombinations.objects.filter(
            product__category__slug=category_slug).all().order_by("-id")
    else:
        products = VariationCombinations.objects.all().filter(
            product__is_active=True).order_by("-id")

    all_cat = VariationCAtegory.objects.all()

    filters = {}

    for cat in all_cat:
        filter_vals = []
        for vars in Variations.objects.filter(variation_category__slug=cat.slug).distinct('value'):
            filter_vals.append(vars.value)
        filters[cat.slug] = filter_vals

    context = {
        "products": products,
        "count": len(products),
        "filters": filters
    }

    return render(req, 'ecommerce/store.html', context=context)


def product_view(req, product_slug):

    product_combo = VariationCombinations.objects.get(slug=product_slug)
    product = product_combo.product
    variation_list = product.variations_set.all()

    vars = {}

    for variation in variation_list:
        if variation.variation_category.name in vars:
            vars[variation.variation_category.name].append(variation.value)
        else:
            vars[variation.variation_category.name] = [variation.value]

    context = {
        "product": product_combo,
        "variations": vars
    }

    return render(req, 'ecommerce/detail.html', context=context)
