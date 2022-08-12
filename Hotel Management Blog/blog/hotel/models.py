from django.db import models
from authentication.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from core.models import post

# Create your models here.
class baseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        
        abstract = True
        
class Amenity(baseModel):
    amenity_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.amenity_name
    
class hotel(baseModel):
    hotel_name = models.CharField(max_length=100)
    hotel_manager = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    hotel_price = models.IntegerField()
    room_count = models.IntegerField(default=10)
    hotel_address = models.CharField(max_length=100)
    hotel_city = models.CharField(max_length=100)
    hotel_phone = models.CharField(max_length=100)
    hotel_email = models.CharField(max_length=100)
    hotel_description = RichTextField(blank=True, null=True)
    hotel_amenities = models.ManyToManyField(Amenity)
    hotel_image = models.ImageField(upload_to = 'images/')
    
    def __str__(self) -> str:
        return self.hotel_name
    
    def get_absolute_url(self):
        # return reverse('index-detailed', args=(str(self.id)))
        return reverse('index')

    
class hotelBooking(baseModel):
    hotel = models.ForeignKey(hotel, related_name="hotel_bookings", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_bookings", on_delete=models.CASCADE)
    booking_start_date = models.DateField()
    booking_end_date = models.DateField()
    booking_type= models.CharField(max_length=100,choices=(('Pre Paid' , 'Pre Paid') , ('Post Paid' , 'Post Paid')))
   