from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    updated_at = models.DateTimeField(auto_now=True)
    inventory = models.IntegerField(default=0)
