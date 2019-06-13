from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify

#choices for choice fields
from .choices import *

# Create your models here.


class Product(models.Model):
    '''
    product model class
    '''
    product_name = models.CharField(_('Product'), max_length=20)
    product_description = models.CharField(_('Product description'), max_length=200)
    slug = models.SlugField()

    #product absolute url
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})    

    # string representation of the product
    def __str__(self):
        return self.product_name


class Price(models.Model):
    '''
    product unit price
    '''

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    unit = models.CharField(_('Unit of measurement'), max_length=5,
                            choices=MEASURING_UNIT_CHOICES, default=KILOGRAM)
    price = models.IntegerField(_('Price per unit'))

    # string representation of the Price
    def __str__(self):
        return str(self.price)

class Quantity(models.Model):
    '''
    product quantity 
    '''
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='quantities')
    unit = models.CharField(_('Unit of measurement'), max_length=5,
                            choices=MEASURING_UNIT_CHOICES, default=KILOGRAM)
    quantity = models.IntegerField(_('Available quantity'))

    # string representation of the Quantity
    def __str__(self):
        return str(self.quantity)

#create product slug
@receiver(pre_save, sender=Product)
def create_product_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.product_name)
