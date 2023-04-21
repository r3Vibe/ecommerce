

from django.urls import path
from .views import store

app_name = "ecommerce"

urlpatterns = [
    path('<slug:category_slug>/', store, name="product_by_category")
]
