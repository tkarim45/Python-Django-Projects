from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
Roles = (
    
    ('Admin', 'Admin'),
    ('HotelManager', 'HotelManager'),
    ('Tourist', 'Tourist')
)

class User(AbstractUser):
    user_type = models.CharField(max_length=20, choices=Roles, default='Admin')
    
    def __str__(self):
        return self.username