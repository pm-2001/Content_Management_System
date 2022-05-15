
from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from blog.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def home(request):
    # return HttpResponse("This is home page")
    if request.user.is_anonymous:
        return redirect("/signin")
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

    # return HttpResponse("This is about page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone = phone, desc=desc, date = datetime.today())
        contact.save()
    return render(request,'contact.html')

    # return HttpResponse("This is contact page")

def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,'signin.html')
    return render(request,'signin.html')

