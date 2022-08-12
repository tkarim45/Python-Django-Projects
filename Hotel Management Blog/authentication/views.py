import email
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.views.generic.edit import CreateView

# Create your views here.

class SignUpViewManager(CreateView):
    form_class = UserForm
    success_url = reverse_lazy("login")
    template_name = "registration/registerManager.html"
    
    def post(self, request):
        if "LoginU" in self.request.method == 'POST':
            print("j2ebjecjejce3jkcj")
            username = request.POST.get('username').lower()
            password = request.POST.get('password')
        
            try:
                user = User.objects.get(username=username)
                
            except:
                messages.warning(request, 'Invalid username or password')
                return redirect(request.META.get('HTTP_REFERER'))

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('index')   
            else:
                messages.warning(request, 'Invalid username or password') 
                return redirect(request.META.get('HTTP_REFERER')) 
    
class SignUpViewTourist(CreateView):
    form_class = UserForm
    success_url = reverse_lazy("login")
    template_name = "registration/registerTourist.html"

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/')
   
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
    
        try:
            user = User.objects.get(username=username)
            
        except:
            messages.warning(request, 'Invalid username or password')
            return redirect(request.META.get('HTTP_REFERER'))

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')   
        else:
            messages.warning(request, 'Invalid username or password') 
            return redirect(request.META.get('HTTP_REFERER'))     
    
    return render(request, 'registration/login.html')

def logoutuser(request):
    logout(request)
    return redirect('index')
