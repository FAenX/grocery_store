from django.shortcuts import render
from django.http import JsonResponse

import json

from store.models import Product, Quantity

# Create your views here.


def product_validate(request):
    '''
    validate items on cart.
    check if order quantities are available in stock
    '''    
    if request.method == 'GET':
        d = {}
        qty=''
        # received data from ajax request
        rdata = json.loads(request.GET.get('cartItems', None))
        for da in rdata:
            name = da['name']
            count = da['count']
            product = Product.objects.filter(product_name=name).values().get()[
                'id']  # filter product id
            quantity = Quantity.objects.filter(pk=product).values().get()[
                'quantity']  # filter product available quantity
            if int(count) <= int(quantity):
                d[name] = True
            else:
                d[name] = False
                qty = quantity

        for k, v in d.items():
            if v is True:
                data = {'is_available': True} #return is_available true if all items pass test
            else:
                data = {
                    'error_message': f"There is only {qty} {k} available, please match the quantity"} #return error if one item fail test
                print(data)
                break

        return JsonResponse(data)


def checkout_done_view(request):
    '''
    render checkout done page
    '''
    return render(request, "cart/checkout.html", {})


def checkout(request):
    '''
    process checkout
    reduce items available etc later
    '''
    if request.method == 'POST':
        items = json.loads(request.POST.get('cartItems', None))
        print(items)
        data = {'accepted': 'Recieved'}
        return JsonResponse(data)

        
