from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from pyexpat import model
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField(null=True)
      
    def __str__(self):
       return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = "images/",null=False,blank=True,default='images/a.png')
    class Meta:
        ordering=['-date']

    def __str__(self):
       return self.title + ' | ' +str(self.username)
       
    def get_absolute_url(self):
        return reverse('home')
    