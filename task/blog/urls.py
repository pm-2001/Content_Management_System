from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns =[
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('posts',views.posts, name='posts'),
    path('register',views.register, name='register'),
    path('signin',views.signin, name='signin'),
    path('logout',views.logoutUser, name='logout'),
]
# password marvel@1234