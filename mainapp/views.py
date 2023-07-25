
from django.contrib.auth import authenticate, login 
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
# Create your views here.

def test(request):
    return render(request,'mainapp/test.html')

def dashboard(request):
    sales = Sales.objects.all()
    categories = Categories.objects.all()
    
    context = {
        "sales":sales,
        "categories":categories,

    }
    return render(request,'mainapp/index.html',context)

def documentation(request):
    return render(request, 'mainapp/documentation.html')

def index(request):
    return render(request, 'mainapp/index.html')

def billing(request):
    return render(request,'mainapp/billing.html')

def signin(request):
    return render(request,'mainapp/sign-in.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')  
        
        user = authenticate(request,username=username,password=password)
      
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,"Username or password was incorrect")
    context = {
           
    }
    return render(request,'mainapp/sign-up.html')

def profile(request):
    return render(request,'mainapp/profile.html')

def table(request):
    tables = Table.objects.all()
    
    context = {
        "tables":tables,
    }
    return render(request,'mainapp/tables.html',context)

def virtual_reality(request):
    return render(request,'mainapp/virtual-reality.html')