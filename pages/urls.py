from django.urls import path, include
from pages import views

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path("", views.home, name='home'),
    path("home", views.home, name='home'),
    path("vendors", views.home, name='home'),
    path("login", views.login_view, name='login'),
    path("logout", views.custom_logout, name='logout'),
    path("validate", views.validateAndRedirect, name='validate'),
    path("dashboard", views.home, name='home'),
    path("productDetail", views.productDetail, name='products'),
    path("vendor", views.vendor, name='vendor'),
    path("updateVendor", views.updateVendor, name='vendor'),

    path("contactUs", views.contactUs, name='contactUs'),
]