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
        items = json.loads(request.GET.get('cartItems', None))
        d = {}
        i = len(items)-1
        
        
        while i >= 0:
            item = items[i]
            product = Product.objects.filter(product_name=item['name']).values().get()['id']
            available_quantity = Quantity.objects.filter(pk=product).values().get()['quantity']
            print(available_quantity)
            print(item['count'])
            if available_quantity >= int(item['count']):
                d[item['name']] = True
            else:
                d[item['name']] = False
                qty = available_quantity
            
            i-=1
        
        for k, v in d.items():
            if v is True:
                data = {'is_available': True} #return is_available true if all items pass test
            else:
                data = {
                    'error_message': f"There is only {qty} {k} available, please match the quantity"} #return error if one item fail test
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
        i = len(items)-1
        print(i)
        
        while i >= 0:
            item = items[i]
            product = Product.objects.filter(product_name=item['name']).values().get()['id']
            print(product)
            available_quantity = Quantity.objects.filter(pk=product).values().get()['quantity']
            new_qty = available_quantity - int(item['count'])
            qty_obj = Quantity.objects.get(pk=product)
            qty_obj.quantity = new_qty
            qty_obj.save()
            i-=1

        print(items)
        data = {'accepted': 'Recieved'}
        return JsonResponse(data)


