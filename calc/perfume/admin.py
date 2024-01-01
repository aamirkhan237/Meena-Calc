from django.contrib import admin
from .models import Product, CustomerOrder


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price_per_gram")


@admin.register(CustomerOrder)
class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = ("product", "grams", "quantity", "discount", "calculate_price")

    def calculate_price(self, obj):
        return obj.calculate_price()

    calculate_price.short_description = "Total Price"
