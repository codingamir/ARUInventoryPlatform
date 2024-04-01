
from django.shortcuts import render
from pages.models import Product
from pages.forms import ProductForm

def productDetail(request):
    product_id = request.GET.get("id")
    product = Product.objects.get(pk=product_id)

    productForm = ProductForm(instance=product)
    return render(request, "pages/products/productDetail.html", {"product": productForm} )