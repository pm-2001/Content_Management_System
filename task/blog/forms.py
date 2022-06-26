
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms
from .models import Post

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password1': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password2': forms.TextInput(attrs={'class': 'form-control'}),
        # }

class ImageForm(forms.ModelForm):
    class Meta:
        model=Post
        fields =['title','username','body','image']
        template_name='post.html'   
        # fields = ('title',)   