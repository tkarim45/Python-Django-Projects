from email import message
from operator import index
import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Message, Room, Topic 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RoomForm


# Create your views here.
def loginpage(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('index')
    
   
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
    
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid username or password')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')   
        else:
            messages.error(request, 'Invalid username or password')            
    
    context = {'page': page}
    return render(request, 'core/login.html', context)


def logoutuser(request):
    logout(request)
    return redirect('index')

def registeruser(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            redirect('index')
            login(request, user)  
            
        else:
            messages.error(request, 'An Error Occurred')
            
    return render(request, 'core/login.html', {'form': form})

def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    rooms = Room.objects.filter(
        Q(topic__text__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
    )
    
    topics = Topic.objects.all()
    rooms_count = rooms.count()
    room_messages = Message.objects.filter(
        Q(room__topic__text__icontains = q) 
    )
    
    
    context = {'rooms': rooms, 'topics': topics, 'room_count': rooms_count, 'room_messages': room_messages}
    return render(request, 'core/home.html', context)

def about(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            message = request.POST.get('message')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)
    
    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'core/room.html', context)


def userprofile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics  = Topic.objects.all()
    context = {'user': user, 'rooms': rooms, 'topics': topics, 'room_messages': room_messages}
    return render(request, 'core/profile.html', context)


@login_required(login_url='login')
def createroom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'core/room_form.html', context)

@login_required(login_url='login')
def updateroom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.user != room.host:
        return HttpResponse('You are not authorized to edit this room')
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('index')
    
    context = {'form': form}
    return render(request, 'core/room_form.html', context)  

@login_required(login_url='login')
def deleteroom(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.user != room.host:
        return HttpResponse('You are not authorized to delete this room')
    
    if request.method == 'POST':
        room.delete()
        return redirect('index')
    return render(request, 'core/delete.html', {'obj':room})


@login_required(login_url='login')
def deletemessage(request, pk):
    message = Message.objects.get(id=pk)
    
    if request.user != message.user:
        return HttpResponse('You are not authorized to delete this room')
    
    if request.method == 'POST':
        message.delete()
        return redirect('index')
    return render(request, 'core/delete.html', {'obj':message})