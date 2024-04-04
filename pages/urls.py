from django.urls import path, include
from views import home, registeration, product, vendor

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path("", home.home, name='home'),
    path("home", home.home, name='home'),
    path("vendors", home.home, name='home'),
    path("login", registeration.login_view, name='login'),
    path("logout", registeration.custom_logout, name='logout'),
    path("validate", registeration.validateAndRedirect, name='validate'),
    path("dashboard", home.home, name='home'),
    path("products", product.products, name='products'),
    path("productDetail", product.productDetail, name='products'),
    path("vendor", vendor.vendor, name='vendor'),
    path("updateVendor", vendor.updateVendor, name='vendor'),

    path("contactUs", registeration.contactUs, name='contactUs'),]
