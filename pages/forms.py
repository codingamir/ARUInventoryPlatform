from django.forms import ModelForm
from .models import Vendor, Product, ProductCapability


class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = ["company_url", "employees_count", "internal_professinal_service", "last_demo", "last_review"]

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class ProductCapabilityForm(ModelForm):
    class Meta:
        model = ProductCapability
        fields = "__all__"
