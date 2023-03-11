from django.contrib import admin
from django.urls import path,include 
from . import views
# from blog import views

urlpatterns = [
   path('products/',views.getAllProducts)
   
]