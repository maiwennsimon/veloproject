from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class BaseModel (models.Model):
    uid=models.UUIDField(default=uuid.uuid4 , editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class State(models.TextChoices):
    GOOD = 'G'
    VERY_GOOD = 'VG'
    PERFECT = 'P'
    NEW = 'N'
    BAD = 'B'





class Bike(BaseModel):

    brand = models.fields.CharField(max_length=100)
    bike_price = models.IntegerField()
    description= models.TextField()
    state = models.fields.CharField(choices=State.choices, max_length=5)
    color = models.fields.CharField(max_length=30)
    bike_count = models.IntegerField(default=10)



    def __str__(self) -> str:
        return self.brand

class bikeImage(BaseModel):
    bike= models.ForeignKey(Bike, related_name="images", on_delete=models.CASCADE)
    images = models.ImageField(upload_to='bike')



class BikeBooking(BaseModel):
    bike= models.ForeignKey(Bike, related_name= "bike_booking", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_booking", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_type = models.CharField(max_length=100, choices=(('Pre-Paid' , 'Pre-Paid'), ('Post-Paid' , 'Post-Paid') ))
