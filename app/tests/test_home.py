from django.test import TestCase, Client
from django.urls import reverse

class HomeViewTest(TestCase):
  def setUp(self):
    self.client = Client()

  def tearDown(self):
    pass

  def test_page(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)