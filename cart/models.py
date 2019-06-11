from django.db import models
# Create your models here.
from store.models import Product


class Cart(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return str(self.id)

