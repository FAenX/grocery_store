from django.urls import path

#app views
from .views import ProductsListView

#store app urls
urlpatterns = [
    path('index/', ProductsListView.as_view(), name='product_list'),
]
