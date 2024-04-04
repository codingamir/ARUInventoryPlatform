from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from pages.models import Vendor, Product
from pages.forms import VendorForm


def vendor(request):
    
    vendor_id = request.GET.get("id")
    vendor = Vendor.objects.get(pk=vendor_id)
    products = Product.objects.filter(Vendor_id = vendor_id)
    return render(request, "pages/vendor/vendor.html", {"vendor": vendor, "products": products} )


def updateVendor(request):
    # if not request.user.is_authenticated:
    #     return redirect("login?next={request.path}")

    if request.method == "GET":
        vendor_id = request.GET.get("id")
        vendor = Vendor.objects.get(pk=vendor_id)
        print(vendor)
        vendorForm = VendorForm(instance=vendor)
        return render(request, "pages/vendor/updateVendor.html", {"vendor": vendorForm} )
    
    vendor_id = request.GET.get("id")
    instance = get_object_or_404(Vendor, pk=vendor_id)
    if request.method == 'POST':
        vendorForm = VendorForm(request.POST, instance=instance)
        if vendorForm.is_valid():
            vendorForm.save()
            vendor_id = request.GET.get("id")
            vendor = Vendor.objects.get(pk=vendor_id)
            vendorForm = VendorForm(instance=vendor)

            return render(request, "pages/vendor/updateVendor.html", {"vendor": vendorForm, "info": "Success: Vendor saved succussfully."} )
        else:
            vendor_id = request.GET.get("id")
            vendor = Vendor.objects.get(pk=vendor_id)
            vendorForm = VendorForm(instance=vendor)

        return render(request, "pages/vendor/updateVendor.html", {"vendor": vendorForm, "info": "Error: Invalid form data. Please correct and try again."} )
