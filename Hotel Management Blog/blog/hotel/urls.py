from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import bookingPage, data, detailHotelView, addHotelPage, deleteHotel, updateHotel




urlpatterns = [

  path('addHotel/<int:pk>', addHotelPage.as_view(), name='addHotel'),
  path('booking/<int:pk>', bookingPage.as_view(), name='booking'),
  path('hotel-detail/<int:pk>' , detailHotelView.as_view() , name="hotel_detail"),
  path('update-content/<int:pk>/remove', deleteHotel.as_view(), name='delete-hotel'),
  path('update-hotel/<int:pk>', updateHotel.as_view(), name='update-hotel'),
  path('update-hotel/edit/<int:pk>', updateHotel.as_view(), name='update-hotel'),
  path('get_data/<int:id>/', data)

]
