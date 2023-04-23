

from django.urls import path
from .views import store_view, product_view

app_name = "ecommerce"

urlpatterns = [
    path('', store_view, name="store"),
    path('category/<slug:category_slug>/',
         store_view, name="product_by_category"),
    path('product/<slug:product_slug>',
         product_view, name="product")
]
