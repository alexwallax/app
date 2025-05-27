from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200) # titulo
    category = models.CharField(max_length=100) # categoria
    brand = models.CharField(max_length=100) # marca
    description = models.TextField(null=True, blank=True) # descrição
    price = models.DecimalField(max_digits=10, decimal_places=2) # preço
