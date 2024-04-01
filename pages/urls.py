from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login", views.login, name='login'),
    path("validate", views.validateAndRedirect, name='validate'),
    path("dashboard", views.home, name='home'),

     path("contactUs", views.contactUs, name='contactUs'),
]
