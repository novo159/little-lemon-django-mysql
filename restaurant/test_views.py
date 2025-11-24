from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import MenuItem


class MenuItemViewTests(APITestCase):
    def setUp(self):
        MenuItem.objects.create(title="Pasta", price=12, inventory=50)

    def test_menu_items_list(self):
        url = reverse('menu-items')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_menu_item_detail(self):
        item = MenuItem.objects.first()
        url = reverse('single-menu-item', args=[item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], item.title)
