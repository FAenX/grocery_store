from django.shortcuts import render
from django.views.generic import ListView 

#app models
from .models import Product

# Create your views here.
class ProductsListView(ListView):
    '''
    product list view
    '''
    template_name = 'index.html'
    model = Product 