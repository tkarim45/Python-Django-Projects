from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.registeruser, name='register'),
    path('', views.index, name='index'),
    path('room/<str:pk>/', views.about, name='room'),
    
    path('profile/<str:pk>/', views.userprofile, name='user-profile'),
    path('create-room/', views.createroom, name='create-room'),
    path('update-room/<str:pk>/', views.updateroom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteroom, name='delete-room'),
    path('delete-message/<str:pk>/', views.deletemessage, name='delete-message')
]