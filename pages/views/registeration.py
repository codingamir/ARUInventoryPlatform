from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.shortcuts import render


def custom_logout(request):
    logout(request)
    return redirect("home")

def login_view(request):
    if not request.user.is_authenticated:
        return render(request, "pages/registration/login3.html")
    return render(request, "pages/home.html", {"user_name": request.user.username})

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


def contactUs(request):
    return render(request, "pages/BecomeVendor/contactUs.html")