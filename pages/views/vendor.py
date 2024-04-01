from django.shortcuts import render
from pages.models import Vendor


def vendor(request):
    vendor_id = request.GET.get("id")
    vendor = Vendor.objects.get(pk=vendor_id)
    return render(request, "pages/vendor/vendor.html", {"vendor": vendor} )
