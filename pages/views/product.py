from django.shortcuts import get_object_or_404, render
from pages.models import Product, ProductCapability
from pages.forms import ProductForm, ProductCapabilityForm

def productDetail(request):
    product_id = request.GET.get("id")
    product = Product.objects.get(pk=product_id)
    productCapability = ProductCapability.objects.filter(Product_id = product_id).first()
    
    productForm = ProductForm(instance=product)
    productCapabilityForm = ProductCapabilityForm(instance=productCapability)
    return render(request, "pages/products/productDetail.html", {"product": productForm, "productCapability": productCapabilityForm} )


def updateProduct(request):
    # if not request.user.is_authenticated:
    #     return redirect("login?next={request.path}")

    if request.method == "GET":
        product_id = request.GET.get("id")
        product = Product.objects.get(pk=product_id)
        print(product)
        productForm = ProductForm(instance=product)
        return render(request, "pages/vendor/updateVendor.html", {"vendor": productForm} )
    
    product_id = request.GET.get("id")
    instance = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        productForm = ProductForm(request.POST, instance=instance)
        if productForm.is_valid():
            productForm.save()
            product_id = request.GET.get("id")
            product = Product.objects.get(pk=product_id)
            productForm = ProductForm(instance=product)

            return render(request, "pages/vendor/updateVendor.html", {"vendor": productForm, "info": "Success: Vendor saved succussfully."} )
        else:
            product_id = request.GET.get("id")
            product = Product.objects.get(pk=product_id)
            productForm = ProductForm(instance=product)

        return render(request, "pages/vendor/updateVendor.html", {"vendor": productForm, "info": "Error: Invalid form data. Please correct and try again."} )
