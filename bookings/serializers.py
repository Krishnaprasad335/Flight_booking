from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Flight,Booking_Ticket

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = [
            'airline',
            'flight_number',
            'departure_city',
            'destination_city',
            'departure_time',
            'arrival_time',
            'price'
            ]

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking_Ticket
        fields = '_all_'    