from django.db import models
from django.conf import settings
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    updated_at = models.DateTimeField(auto_now=True)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    # product_set

class Collection(models.Model):
    title = models.CharField(max_length=100)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='collections')

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Order(models.Model):
    ORDER_STATUS = (
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('F', 'Filled'),
    )
    #user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    placed_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=ORDER_STATUS, default='P')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=6)
