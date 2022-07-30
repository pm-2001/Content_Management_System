from django.contrib import admin
from blog.models import Contact,Comment,Profile
from blog.models import Post

# Register your models here.
admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
