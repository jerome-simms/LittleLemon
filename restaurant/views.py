from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

def index(request):
    return render(request, 'index.html')

################
# MENU ITEMS API
################

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


#############
# BOOKING API
#############

class BookingVewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer