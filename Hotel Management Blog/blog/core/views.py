from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import post
from .forms import postform


    

# Create your views here.
class indexPage(ListView):
    model = post
    template_name = 'index.html'
    ordering = ['-date_posted']
    
class indexPageDetailed(DetailView):
    model = post
    template_name = 'indexDetailed.html'
    
class addContent(CreateView):
    model = post
    form_class = postform
    template_name = 'post.html'
    # fields = ['title', 'content']
    
class updateContent(UpdateView):
    model = post
    form_class = postform
    template_name = 'updatePost.html'
    # fields = ['title', 'content']
    
class deleteContent(DeleteView):
    model = post
    template_name = 'deletePost.html'
    success_url = '/'
    
class aboutuspage(ListView):
    model = post
    template_name = 'aboutuspage.html'
    