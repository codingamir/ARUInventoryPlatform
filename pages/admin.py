from django.contrib import admin

from .models import User

# Register your models here.


class UserRepresentation(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "email",)

admin.site.register(User, UserRepresentation)