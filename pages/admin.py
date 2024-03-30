from django.contrib import admin

from .models import User, Vendor, ProductCapability, Product

# Register your models here.


class UserRepresentation(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "email",)

class VendorRepresentation(admin.ModelAdmin):
  list_display = ("company_name",)

class ProductRepresentation(admin.ModelAdmin):
  list_display = ("product_name",)

admin.site.register(User, UserRepresentation)

admin.site.register(Vendor, VendorRepresentation)

admin.site.register(ProductCapability)

admin.site.register(Product, ProductRepresentation)

