from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    updated_at = models.DateTimeField(auto_now=True)
    inventory = models.PositiveIntegerField()

class Collection(models.Model):
    title = models.CharField(max_length=100)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    quantity = models.PositiveIntegerField()

class Order(models.Model):
    ORDER_STATUS = (
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('F', 'Filled'),
    )
    placed_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=ORDER_STATUS, default='P')

class OrderItem(models.Model):
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=6)
