from django.urls import path
from .views import RegisterView, LoginView
from .views import FlightSearchView, FlightBookingView,PastBookingsView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('flights/', FlightSearchView.as_view(), name='flight_search'),
    path('flights/book/<int:flight_id>/', FlightBookingView.as_view(), name='flight_booking'),
    path('flights/pastbooking/', PastBookingsView.as_view(), name='flight_past_booking'),
    
]