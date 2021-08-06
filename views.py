from django.shortcuts import render
from django.http import HttpResponse
from .form import wishlist
from .models import user,product
def home(request):
    form=wishlist()
    if request.method=='POST':
        form=wishlist(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'FLIPKARTAPP/home.html',context)
def register(request):
    form=wishlist()
    if request.method=='POST':
        form=wishlist(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'FLIPKARTAPP/register.html',context)

def login(request):
    form=wishlist()
    if request.method=='POST':
        form=wishlist(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'FLIPKARTAPP/login.html',context)
