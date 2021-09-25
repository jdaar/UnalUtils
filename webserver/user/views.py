from user.serializers import UserSerializer
from user.models import User
from django.shortcuts import render
from rest_framework import generics

# Create your views here.


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
