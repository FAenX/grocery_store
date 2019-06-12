from django.urls import path

# SHOPING CART VIEWS
from .views import (
    checkout_done_view, product_validate, checkout
)


urlpatterns = [
    path('checkout/success/', checkout_done_view,
         name='success'),  # checkout success url
    path('api/product-validate/', product_validate,
         name='validate'),  # shoping cart validation url
    # shopping cart checkout endpoint
    path('api/checkout/', checkout, name='checkout')
]
