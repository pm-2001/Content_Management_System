
from ast import Subscript
from audioop import reverse
from django.shortcuts import render,HttpResponse,redirect,get_list_or_404
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
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages


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

class DeletePostView(DeleteView):
    model= Post
    template_name = 'delete_post.html'
    success_url= reverse_lazy('myblogs')

def about(request):
    return render(request,'about.html')

    # return HttpResponse("This is about page")
@login_required(login_url='signin')
def posts(request):
    user=request.user
    form = ImageForm(initial={'username':user})
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            return redirect("/")      
    #     title = request.POST.get('title')
        # username = request.POST.get(request.user)
    #     body = request.POST.get('body')
        # posts= Post(username=request.user.username,date = datetime.today())
        # posts.save()
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
        messages.success(request,'Submitted successfully')
    return render(request,'contact.html')


    # return HttpResponse("This is contact page")

def register(request):
    form = CreateUserForm()
      
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account has been created successfully')
            return redirect('signin')
        else:
            messages.success(request,"password didn't match!")
            return render(request,'register.html')
        # if user is not None:
        #     login(request,user)
        #     return redirect("/")
        # else:
        #     return render(request,'signin.html')
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
            messages.success(request,'Username or password is incorrect!')
            return render(request,'signin.html')
    return render(request,'signin.html')

def logoutUser(request):
    logout(request)
    return render(request,'signin.html')

@login_required(login_url='signin')
def myblogs(request):
    user=request.user

    posts = user.post_set.filter(username=user)
    return render(request,'myblogs.html',{'posts':posts})

def LikeView(request,pk):
    post=get_list_or_404(Post,id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('postdetail' , args=[str(pk)]))