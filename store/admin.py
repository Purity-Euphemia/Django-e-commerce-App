from django.contrib import admin
from .models import Product
# Register your models here.

# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','updated_at']

    list_per_page = 10
    search_fields = ['title','description']
