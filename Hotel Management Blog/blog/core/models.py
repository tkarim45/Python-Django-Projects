from django.db import models
from authentication.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    Image = models.ImageField(blank = True, null = True, upload_to = 'images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # return reverse('index-detailed', args=(str(self.id)))
        return reverse('index')
    
   
    
