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
    list_display = ['product_name', 'quantity', 'price']
    inlines = [QuantityInline, PriceInline]

    def quantity(self, product):
        return product.quantities.all()[0]
    def price(self, product):
        return product.prices.all()[0]

    
    
    


