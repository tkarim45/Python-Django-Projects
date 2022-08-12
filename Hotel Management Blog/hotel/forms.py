from django import forms
from .models import hotel


class hotelForm(forms.ModelForm):
    class Meta:
        model = hotel
        fields = ['hotel_name', 'hotel_manager' ,'hotel_price', 'room_count', 'hotel_address', 'hotel_phone', 'hotel_email', 'post','hotel_description', 'hotel_amenities', 'hotel_image']
        
        widgets = {
            'hotel_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Hotel Name'}),
            'hotel_manager': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author', 'value': '', 'id': 'hotelManager', 'type': 'hidden'}),
            'hotel_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price'}),
            'room_count': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Total Number of Rooms'}),
            'hotel_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
            'hotel_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'hotel_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'post': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'hotel_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}),
        }