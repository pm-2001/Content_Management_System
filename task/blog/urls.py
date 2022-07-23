from django.contrib import admin
from django.urls import path
from blog import views
from blog.views import PostDetail,UpdatePostView,DeletePostView,LikeView

urlpatterns = [
    path('',views.home, name='home'),
    path('article/<int:pk>',PostDetail.as_view(),name='postdetail'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('posts/',views.posts, name='posts'),
    path('register',views.register, name='register'),
    path('signin',views.signin, name='signin'),
    path('logout',views.logoutUser, name='logout'),
    path('article/edit/<int:pk>',views.UpdatePostView.as_view(),name='update_post'),
    path('article/delete/<int:pk>',views.DeletePostView.as_view(),name='delete_post'),
    path('myblogs',views.myblogs, name='myblogs'),
    path('like/<int:pk>', LikeView , name='like_post'),
]