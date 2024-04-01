
from django.shortcuts import render
from pages.models import Product, ProductCapability
from pages.forms import ProductForm, ProductCapabilityForm

def productDetail(request):
    product_id = request.GET.get("id")
    product = Product.objects.get(pk=product_id)
    productCapability = ProductCapability.objects.filter(Product_id = product_id).first()
    
    productForm = ProductForm(instance=product)
    productCapabilityForm = ProductCapabilityForm(instance=productCapability)
    return render(request, "pages/products/productDetail.html", {"product": productForm, "productCapability": productCapabilityForm} )
