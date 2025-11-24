from datetime import datetime

from django.test import TestCase
from django.utils.timezone import make_aware

from .models import Booking, MenuItem


class MenuItemModelTests(TestCase):
    def test_string_representation(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")


class BookingModelTests(TestCase):
    def test_string_representation(self):
        booking_time = make_aware(datetime(2025, 1, 1, 18, 0))
        booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=2,
            booking_date=booking_time,
        )
        self.assertIn("John Doe", str(booking))
        self.assertIn("2025", str(booking))
