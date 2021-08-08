from factory import Faker
from factory.django import DjangoModelFactory
from django.test import TestCase
from ..models import User

class UserFactory(DjangoModelFactory):
  name = Faker('company')
  description = Faker('text')

  class Meta:
    model = User

class UserTestCase(TestCase):
  def test_str(self):
    """Test for string representation."""
    user = UserFactory()
    self.assertEqual(str(user), user.name)