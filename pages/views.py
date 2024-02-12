from django.shortcuts import render

from .models import User

# Create your views here.


def home(request):
    return render(request, "pages/home.html", {})

def login(request):
    return render(request, "pages/registration/login.html")

def validateAndRedirect(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    if email == "" or password == "":
        return render(request, "pages/registration/login.html", {"invalid_details": "username or password cannot be empty!"})
    
    user = User.objects.filter(email = email, password = password).first()

    if user == None:
        return render(request, "pages/registration/login.html", {"invalid_details": "username or password is invalid!"})
    return render(request, "pages/home.html")