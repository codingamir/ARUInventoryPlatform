from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
