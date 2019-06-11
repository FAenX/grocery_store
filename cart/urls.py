from django.urls import path

from .views import (
    checkout_done_view, product_validate
)


urlpatterns = [
    path('checkout/success/', checkout_done_view, name='success'),
    path('api/product-validate/', product_validate, name='validate')
]
