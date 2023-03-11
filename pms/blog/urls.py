from django.contrib import admin
from django.urls import path,include 
from .import views

urlpatterns = [

    path('index/',views.index),
    path('aboutus/',views.aboutUs),
    path('contactus/',views.contactus),
    path('feedback/',views.feedback),
]
