from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("gym:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Stronger")
        self.assertContains(response, "Modern Equipment")
