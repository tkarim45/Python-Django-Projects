from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .models import (Amenity, hotel, hotelBooking)
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import hotelForm


# Create your views here.
class deleteHotel(DeleteView):
    model = hotel
    template_name = 'hotelreg/deleteHotel.html'
    success_url = '/'
    
class updateHotel(UpdateView):
    model = hotel
    form_class = hotelForm
    template_name = 'hotelreg/updateHotel.html'


class bookingPage(ListView):
    model = hotel
    template_name = 'hotelreg/booking.html'
    
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        hotel_ = hotel.objects.filter(post=id)
        print(hotel_)
        return render(request, self.template_name, {'hotel': hotel_})
    
class detailHotelView(DetailView): 
    model = hotel
    template_name = 'hotelreg/hotel_detail.html'
    
    def post(self, request, *args, **kwargs):
        hotel_ = ""
        checkin = request.POST.get('checkin')
        checkout= request.POST.get('checkout')
        hotels = hotel.objects.get(id = kwargs['pk'])
        if not check_booking(checkin ,checkout  , kwargs['pk'] , hotels.room_count):
            messages.warning(request, 'Hotel is already booked in these dates ')
            return redirect(request.META.get('HTTP_REFERER'))

        hotelBooking.objects.create(hotel=hotels , user = request.user , booking_start_date=checkin
        , booking_end_date = checkout , booking_type  = 'Pre Paid')
        
        messages.success(request, 'Your booking has been saved')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    

    
class addHotelPage(CreateView):
    model = hotel
    form_class = hotelForm
    template_name = 'hotelreg/addHotel.html'


def check_booking(start_date  , end_date ,pk , room_count):
    
    qs = hotelBooking.objects.filter(
        booking_start_date__gte = start_date,
        booking_end_date__lte = end_date,
        hotel__id = pk
        )

    print(len(qs))
    print("-----------------------------------------\n\n")
    
    if len(qs) >= room_count:
        return False
    
    return True


def data(re, id):
    print(id)
    return HTTPResponse('welcome')
