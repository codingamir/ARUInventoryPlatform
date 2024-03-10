from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.shortcuts import redirect

import inventory_portal


def home(request):
    if not request.user.is_authenticated:
        return redirect("login?next={request.path}")
    return render(request, "pages/home.html", {"user_name": request.user.username})

def login_view(request):
    return render(request, "pages/registration/login.html")

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