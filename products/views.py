from django.shortcuts import render
from products.models import Product #importando a tabela de produtos.


def product_view(request):
    products = Product.objects.all() # SELECT * FROM PRODUCTS - no banco de dados
    
    return render(
        request=request,
        template_name='products.html',
        context={'products': products} # envia os dados do DB para o template
    )



