from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('postComment', views.postComment, name="postComment"),
    path('', views.bloghome, name='bloghome'),
    path('<str:slug>', views.blogpost, name='blogpost')
]