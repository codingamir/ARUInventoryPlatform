from django.shortcuts import render
from pages.models import Vendor


def home(request):
    vendors = Vendor.objects.all()
    return render(request, "pages/home.html", {"user_name": request.user.username, "vendors": vendors} )
