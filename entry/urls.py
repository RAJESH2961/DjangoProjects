from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('about/', views.about, name='about'),
    path('chicken/', views.chicken, name='chicken'),
    path('register/', views.register, name='register'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
]
