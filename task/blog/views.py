
from ast import Subscript
from audioop import reverse
from xml.etree.ElementTree import Comment
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from datetime import datetime
from blog.models import Post,Comment,Contact,Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from .forms import ImageForm,CommentForm,CreateUserForm,EditProfileForm,PasswordChangingForm
from django.views.generic import DetailView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import generic
from django.contrib.auth.views import PasswordChangeView


def home(request):
    # return HttpResponse("This is home page")
    # if request.user.is_anonymous:
    #     return redirect("/register")
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def LikeView(request, pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('postdetail' , args=[str(pk)]))

class PostDetail(DetailView):
    model = Post
    template_name = 'postdetail.html'

    def get_context_data(self,*args,**kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        stuff=get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False

        if stuff.likes.filter(id = self.request.user.id).exists():
            liked=True

        context["total_likes"] = total_likes
        context[" liked "] = liked
        return context

class UpdatePostView(UpdateView):
    model= Post
    template_name = 'update_post.html'
    fields = ['title','body','image']
    success_url= reverse_lazy('myblogs')

class DeletePostView(DeleteView):
    model= Post
    template_name = 'delete_post.html'
    success_url= reverse_lazy('myblogs')

# def delete_post(request,post_id=None):
#     post_to_delete=Post.objects.get(id=post_id)
#     post_to_delete.delete()
#     return render(request,'myblogs.html')

def about(request):
    return render(request,'about.html')

def profile(request):
    profiles = Profile.objects.all()
    return render(request,'profile.html',{'profiles':profiles})
    
@login_required(login_url='signin')
def posts(request):
    user=request.user
    form = ImageForm(initial={'username':user})
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            messages.success(request,'Post created successfully')
            return redirect("myblogs")
        else:
            messages.success(request,'Invalid Post') 
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
    context = {'form':form}
    return render(request,'register.html',context)

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name='edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

def password_success(request):
    return render(request,'password_success.html')

class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangingForm
    success_url = reverse_lazy('password_success')
    # success_url = reverse_lazy('home')

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
    return redirect("/")

@login_required(login_url='signin')
def myblogs(request):
    user=request.user

    posts = user.post_set.filter(username=user)
    return render(request,'myblogs.html',{'posts':posts})


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name= 'addcomment.html'
    # fields= '__all__'
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url= reverse_lazy('home') 
