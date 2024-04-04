import os
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.validators import URLValidator

fs = FileSystemStorage(location='pages/static')

def company_profile_upload_path(instance, path):
    return os.path.join(
        "media/vendor/profiles", 
        path
    )

def company_background_upload_path(instance, path):
    return os.path.join(
        "media/vendor/backgrounds", 
        path
    )

def product_image_upload_path(instance, path):
    return os.path.join(
        "media/product/images", 
        path
    )

class User(models.Model):
    user_id = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class Vendor(models.Model):
    company_name =  models.CharField(max_length=200)
    established =  models.CharField(max_length=200)
    employees_count =  models.IntegerField()
    internal_professinal_service = models.BooleanField()
    last_demo = models.DateField()
    last_review = models.DateField()
    company_dispaly_picture = models.ImageField(default='', storage=fs, upload_to=company_profile_upload_path)
    company_background_picture = models.ImageField(default='', storage=fs, upload_to=company_background_upload_path)
    company_url = models.URLField(default='')
    contact_tel_number = models.CharField(default='', max_length=200)

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(default='', storage=fs, upload_to=product_image_upload_path)
    Vendor = models.ForeignKey(Vendor, default=1, on_delete=models.DO_NOTHING)

class ProductCapability(models.Model):
    business_area = models.CharField(max_length=200)
    modules = models.CharField(max_length=200)
    financial_services_client_types = models.CharField(max_length=200)
    cloud = models.CharField(max_length=200)
    Product = models.ForeignKey(Product, default = 1, on_delete=models.DO_NOTHING)