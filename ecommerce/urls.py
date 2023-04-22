

from django.urls import path
from .views import store_view

app_name = "ecommerce"

urlpatterns = [
    path('', store_view, name="store"),
    path('<slug:category_slug>/', store_view, name="product_by_category")
]
