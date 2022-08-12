from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from .views import SignUpViewManager, SignUpViewTourist
from django.contrib.auth import authenticate


urlpatterns = [
   
   # path('register/',userRegisterView.as_view(), name='register'),
   path('manager-login/', SignUpViewManager.as_view(), name='manager-login'),
   path('registerTourist/', SignUpViewTourist.as_view(), name='registerTourist'),
   path('login/', views.loginpage, name='login'),
   path('logout/', views.logoutuser, name='logout'),
   # path('manager-login/', auth_views.LoginView.as_view(template_name='registration/registerManager.html'), name='manager-login'),
   # path('registerTourist/', auth_views.LoginView.as_view(template_name='registration/registerTourist.html'), name='registerTourist'),
]