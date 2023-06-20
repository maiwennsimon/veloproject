from django.contrib import admin
from .models import bikeImage, Bike, BikeBooking

# Register your models here.
admin.site.register(bikeImage)
admin.site.register(Bike)
admin.site.register(BikeBooking)