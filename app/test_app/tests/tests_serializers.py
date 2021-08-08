from django.test import TestCase
from ..serializers import UserSerializer
from .tests_models import UserFactory

class UsersSerializer(TestCase):
  def test_model_fields(self):
    user = UserFactory()
    serializer = UserSerializer(user)
    for field_name in ['id', 'name', 'description']:
      self.assertEqual(serializer.data[field_name], getattr(user, field_name))