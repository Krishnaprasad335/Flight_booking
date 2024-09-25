from django.contrib import admin
from .models import *
admin.site.register(Flight)
admin.site.register(Booking_Ticket)

# Register your models here.

class FlightModelAdmin(admin.ModelAdmin):
    list_display=['airline','flight_number','departure_city','destination_city','departure_time','arrival_time','price']
   
class Booking_TicketModelAdmin(admin.ModelAdmin):
    list_display=['user','flight','seat_number','booking_status']    
    


