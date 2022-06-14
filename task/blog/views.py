
from ast import Subscript
from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from blog.models import Contact
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .forms import ImageForm
from django.views.generic import DetailView,UpdateView,DeleteView


def home(request):
    # return HttpResponse("This is home page")
    # if request.user.is_anonymous:
    #     return redirect("/register")
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})

class PostDetail(DetailView):
    model = Post
    template_name = 'postdetail.html'

class UpdatePostView(UpdateView):
    model= Post
    template_name = 'update_post.html'
    fields = ['title','body','image']

class DeletePostView(UpdateView):
    model= Post
    template_name = 'update_post.html'
    fields = ['title','body','image']

def about(request):
    return render(request,'about.html')

    # return HttpResponse("This is about page")
@login_required(login_url='signin')
def posts(request):
    form = ImageForm()
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()       
    #     title = request.POST.get('title')
        # username = request.POST.get(request.user)
    #     body = request.POST.get('body')
        # posts= Post(username=request.user,date = datetime.today())
    #     posts.save() 
    context = {'form':form}
    return render(request,'posts.html',context)

@login_required(login_url='signin')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone = phone, desc=desc,date = datetime.today())
        contact.save()
    return render(request,'contact.html')


    # return HttpResponse("This is contact page")

def register(request):
    form = CreateUserForm()
      
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        # # user = authenticate(password1= "password2")
        # if (password1=password2):    
        #     return redirect("/")
        # else:
        #     return render(request,'register.html')
    context = {'form':form}
    return render(request,'register.html',context)

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

def logoutUser(request):
    logout(request)
    return render(request,'signin.html')
