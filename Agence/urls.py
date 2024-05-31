from django.urls import path,include
from django import views
from .views import*


urlpatterns = [
    
    path('',  home, name="home"),
    path('login',  login, name="login"),
    path('register',  register, name="register"), 
    
    
]