from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import redirect
from pages.models import Vendor, Product, ProductCapability
from pages.forms import VendorForm, ProductForm, ProductCapabilityForm


def home(request):
    # if not request.user.is_authenticated:
    #     return redirect("login?next={request.path}")
    
    vendors = Vendor.objects.all()
    return render(request, "pages/home.html", {"user_name": request.user.username, "vendors": vendors, "loggedInUser": request.user.id} )

def vendor(request):
    # if not request.user.is_authenticated:
    #     return redirect("login?next={request.path}")
    
    vendor_id = request.GET.get("id")
    vendor = Vendor.objects.get(pk=vendor_id)
    products = Product.objects.filter(Vendor_id = vendor_id)
    return render(request, "pages/vendor/vendor.html", {"vendor": vendor, "products": products} )

def productDetail(request):
    product_id = request.GET.get("id")
    product = Product.objects.get(pk=product_id)
    productCapability = ProductCapability.objects.filter(Product_id = product_id).first()

    productForm = ProductForm(instance=product)
    productCapabilityForm = ProductCapabilityForm(instance=productCapability)
    return render(request, "pages/products/productDetail.html", {"product": productForm, "productCapability": productCapabilityForm} )

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


    
    

def products(request):
    if not request.user.is_authenticated:
        return redirect("login?next={request.path}")
    return render(request, "pages/products/products.html", {"user_name": request.user.username})

def contactUs(request):
    return render(request, "pages/BecomeVendor/contactUs.html")


def login_view(request):
    if not request.user.is_authenticated:
        return render(request, "pages/registration/login3.html")
    return render(request, "pages/home.html", {"user_name": request.user.username})

def custom_logout(request):
    logout(request)
    return redirect("home")

def validateAndRedirect(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    user = authenticate(request, username=email, password=password)

    if user == None:
        return render(request, "pages/registration/login.html", {"invalid_details": "username or password is invalid!"})

    login(request, user)    
    nxt = request.POST.get("next")

    if nxt is not None:
        return redirect(nxt)
    return redirect("home")