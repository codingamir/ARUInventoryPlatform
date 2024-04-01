from django.shortcuts import render
from pages.models import Vendor, Product


def vendor(request):
    
    vendor_id = request.GET.get("id")
    vendor = Vendor.objects.get(pk=vendor_id)
    products = Product.objects.filter(Vendor_id = vendor_id)
    return render(request, "pages/vendor/vendor.html", {"vendor": vendor, "products": products} )