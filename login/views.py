from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse

def loginPage(request):


    return render(request, "login.html")

def login(request):
    return render(request, "testLogin.html")