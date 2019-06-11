from django.shortcuts import render, redirect
from django.http import JsonResponse

import json

from .models import Cart
from store.models import Product, Quantity
# Create your views here.
def product_validate(request):
    d = {}
    
    rdata = json.loads(request.GET.get('mydata' ,None))
    for da in rdata:        
        name = da['name']
        count = da['count']
        product = Product.objects.filter(product_name=name).values().get()['id']
        quantity = Quantity.objects.filter(pk=product).values().get()['quantity']
        if int(count) <= int(quantity):
            d[name] = True
        else: d[name] = False
    
    for k, v in d.items():
        if v is True:
            data = {'is_available': True}
        else:
            data = {'error_message': f"{k}. in store is less than requested, please reduce quantity"}
            print(data)
            break
            
         
        
    return JsonResponse(data)

def checkout_done_view(request):
    return render(request, "carts/checkout-done.html", {})