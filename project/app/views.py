from django.shortcuts import render
from app.forms import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        response=render(request,'register.html')
        response.set_cookie('fname',fname)
        response.set_cookie('lname',lname)
        response.set_cookie('email',email)
        return response
    return render(request,'register.html')

def login(request):
    print(request.POST)
    if request.method=='POST':
        fname=request.POST.get('fname')
        email=request.POST.get('email')
        print(fname,email)
        response=render(request,'get.html')
        fname=request.COOKIES['fname']
        email=request.COOKIES['email']
        if email==email:
            data={
                'fname':fname,
                'email':email
                }
        return render(request,'get.html',data)
    return render(request,'login.html')
    

def delete(request):
    data=render(request,'delete.html')
    data.delete_cookie('fname')
    data.delete_cookie('lname')
    data.delete_cookie('email')
    return data