from django.urls import path
from .views import generate_trip

urlpatterns = [
    path('trip/', generate_trip, name='generate_trip'),
]
