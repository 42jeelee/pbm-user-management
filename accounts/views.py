from django.shortcuts import render
from rest_framework import generics

from accounts.models import User
from accounts.serializers import UserSerializer

# Create your views here.
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
