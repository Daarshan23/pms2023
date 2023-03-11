from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(req):
    return HttpResponse("HOME")

def index(req):
     return HttpResponse("Hello world!")
def aboutUs(req):
    return render(req,'aboutus.html')
def contactus(req):
    name = "darshan"
    email = "darshan@gmail.com"
    return render(req,'blog/contactus.html',{'name':name,'email':email})

def feedback(req):
    
    userName = "darshan"
    userEmail = "darshan@gmail.com"
    context={
        'userName':userName,
        'userEmail':userEmail,
    }
    
    return render(req,'blog/feedback.html',context)
