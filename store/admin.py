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
        return f"{product.quantities.all().values().get()['quantity']} {product.quantities.all().values().get()['unit']}"
    def price_list(self, product):
        return f"{product.prices.all().values().get()['currency']}  {product.prices.all().values().get()['price']}"