from django.shortcuts import render

from shop.models import Product


# Create your views here.


def product(request, pk):
    object_product = Product.objects.get(pk=pk)
    context = {
        'object_product': object_product,
        'title': object_product.name
    }

    return render(request, 'shop/product.html', context)


def product_list(request):
    products = Product.objects.all()
    context = {
        'object_list': products,
        'title': 'Главная'
    }

    return render(request, 'shop/index.html', context)
