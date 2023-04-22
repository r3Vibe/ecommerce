from django.shortcuts import render
from .models import VariationCAtegory, Variations, VariationCombinations
from django.db.models import Q
# Create your views here.


# def store_view(req, category_slug=None):
#     if req.GET.get('colour') is not None:
#         prducts = Variations.objects.filter(
#             value__iexact=req.GET.get('colour')).all()
#     elif category_slug is not None:
#         prducts = Product.objects.filter(
#             category__slug=category_slug).all().order_by('-id')
#     else:
#         prducts = Product.objects.all().order_by('-id')

#     count = 0
#     for item in prducts:
#         if not item.has_variation:
#             count += 1
#         else:
#             for var in item.variationcombinations_set.all():
#                 count += 1

#     all_cat = VariationCAtegory.objects.all()

#     filters = {}

#     for cat in all_cat:
#         filter_vals = []
#         for vars in Variations.objects.filter(variation_category__slug=cat.slug).distinct('value'):
#             filter_vals.append(vars.value)
#         filters[cat.slug] = filter_vals

#     context = {
#         "products": prducts,
#         "count": count,
#         "filters": filters
#     }

#     return render(req, 'ecommerce/store.html', context=context)

import operator
from functools import reduce


def store_view(req, category_slug=None):
    if category_slug is not None:
        products = VariationCombinations.objects.filter(
            product__category__slug=category_slug).all().order_by("-id")
    elif req.GET.get('colour'):
        colours = req.GET.getlist('colour')
        condition = reduce(
            operator.and_, [Q(variations__value__icontains=s) for s in colours])
        products = VariationCombinations.objects.filter(
            condition).all().order_by("-id")
        print(products)
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
