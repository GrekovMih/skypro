from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product


@login_required
def product_table(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products/product_table.html", context)
