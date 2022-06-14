from django.contrib import admin
from django.urls import path
from blog import views
from blog.views import PostDetail

urlpatterns = [
    path('',views.home, name='home'),
    path('article/<int:pk>',PostDetail.as_view(),name='postdetail'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('posts/',views.posts, name='posts'),
    path('register',views.register, name='register'),
    path('signin',views.signin, name='signin'),
    path('logout',views.logoutUser, name='logout'),
]