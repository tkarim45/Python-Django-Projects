from django import views
from django.urls import path, include
from . import views
from .views import indexPage, indexPageDetailed, addContent, updateContent, deleteContent, aboutuspage

urlpatterns = [
    path('', indexPage.as_view(), name='index'),
    path('index-detailed/<int:pk>', indexPageDetailed.as_view(), name='index-detailed'),
    path('add-content/', addContent.as_view(), name='add-content'),
    path('update-content/<int:pk>', updateContent.as_view(), name='update-content'),
    path('update-content/edit/<int:pk>', updateContent.as_view(), name='update-content'),
    path('update-content/<int:pk>/remove', deleteContent.as_view(), name='delete-content'),
    path('aboutus', aboutuspage.as_view(), name='aboutus'),

    # path('login/', views.loginpage, name='login'),
    # path('logout/', views.logoutuser, name='logout'),
    # path('', views.index, name='index'),
    # path('about-page/', views.aboutpage, name='about-page'),
]