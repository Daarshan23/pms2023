from django.shortcuts import render
from .models import Product

# Create your views here.
def getAllProducts(request):
    
    products = Product.objects.all().values()
    print(products)
    return render (request,'product/allproducts.html',{'products':products})