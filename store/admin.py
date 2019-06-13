from django.contrib import admin

#app models
from .models import Product, Price, Quantity

# Register your models here.
class QuantityInline(admin.TabularInline):
    model = Quantity

class PriceInline(admin.TabularInline):
    model = Price

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'quantities', 'price_list']
    inlines = [QuantityInline, PriceInline]

    def quantities(self, product):
        return [ i for i in product.quantities.all() ]
    def price_list(self, product):
        return [ i for i in product.prices.all() ]

    
    
    


