from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Flight(models.Model):
    airline = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=10)
    departure_city = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=15, decimal_places=3)
    is_active=models.BooleanField(null=False,blank=False,default=True)
    
    def __str__(self):
        return self.airline

class Booking_Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)
    booking_status = models.CharField(max_length=20, default='available')
    


