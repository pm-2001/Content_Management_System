from pyexpat import model
from django.db import models
from django.forms import CharField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField(null=True)
      
    # def _str_(self):
    #    return self.name