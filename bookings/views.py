from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from .models import Flight,Booking_Ticket
from .serializers import FlightSerializer, TicketSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class FlightSearchView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        flights=Flight.objects.filter(is_active=True)
        serializer = FlightSerializer(flights, many=True ).data
        return Response(serializer)
    
class FlightBookingView(APIView):
    permission_classes = [IsAuthenticated]
    
    
    def post(self, request, flight_id):
        flight = Flight.objects.get(id=flight_id)
        seat_number = request.data.get('seat_number')
        
        if Booking_Ticket.objects.filter(flight=flight, seat_number=seat_number).exists():
            return Response({"message": "Seat already booked"}, status=status.HTTP_400_BAD_REQUEST)
        
        ticket = Booking_Ticket(user=request.user, flight=flight, seat_number=seat_number)
        ticket.save()
        return Response({"message": "Booking successful"}, status=status.HTTP_201_CREATED)    
    
  
class PastBookingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tickets = Booking_Ticket.objects.filter(user=request.user)
        serializer = TicketSerializer(tickets, many=True).data
        return Response(serializer)            