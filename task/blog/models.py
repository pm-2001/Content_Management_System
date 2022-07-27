from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from pyexpat import model
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

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
    title = models.CharField(max_length=50,null=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    body = RichTextUploadingField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = "images/",null=True,blank=True,default='images/default.png')
    likes = models.ManyToManyField(User,related_name='blog_post')

    class Meta:
        ordering=['-date']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
       return self.title + ' | ' +str(self.username)
       
    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return '%s - %s' %(self.post.title, self.name)
    