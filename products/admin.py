from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'brand', 'price') # campo de lista
    search_fields = ('title', ) # campo de busca por titulo     
    list_filter = ('category', 'brand') # listar os filtros

admin.site.register(models.Product, ProductAdmin)