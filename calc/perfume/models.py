from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price_per_gram = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class CustomerOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    grams = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def calculate_price(self):
        price = self.product.price_per_gram * self.grams * self.quantity
        discounted_price = price * (1 - self.discount / 100)
        return discounted_price

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units ({self.grams} grams)"
