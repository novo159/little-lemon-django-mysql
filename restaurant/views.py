from django.shortcuts import render
from rest_framework import generics, permissions, viewsets

from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer


def index(request):
	"""Render landing page."""
	return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
	queryset = MenuItem.objects.all()
	serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
	queryset = MenuItem.objects.all()
	serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	permission_classes = [permissions.IsAuthenticated]
