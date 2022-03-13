from typing import List
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from accounts.models import CustomUser
from app.models import *
from .serializers import *

class CustomUserAPIView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class HotelAPIView(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RestourantAPIView(ListAPIView):
    queryset = Restourant.objects.all()
    serializer_class = RestourantSerializer

class CafeAPIView(ListAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class HotelMenuAPIView(ListAPIView):
    queryset = HotelMenu.objects.all()
    serializer_class = HotelMenuSerializer

class RestourantMenuAPIView(ListAPIView):
    queryset = RestourantMenu.objects.all()
    serializer_class = RestourantMenuSerializer

class CafeMenuAPIView(ListAPIView):
    queryset = CafeMenu.objects.all()
    serializer_class = CafeMenuSerializer
