from django.shortcuts import render
from rest_framework.mixins import (
  CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from .models import User
from .serializers import UserSerializer

def HomeView(request):
  return render(request, "home.html")

class UserViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin): 
  serializer_class = UserSerializer
  queryset = User.objects.all()
