from django.urls import path
from .views import CafeAPIView, CafeMenuAPIView, CustomUserAPIView, HotelAPIView, HotelMenuAPIView, RestourantAPIView, RestourantMenuAPIView

urlpatterns = [
    path('users/', CustomUserAPIView.as_view()),
    path('hotels/', HotelAPIView.as_view()),
    path('restourants/', RestourantAPIView.as_view()),
    path('cafes/', CafeAPIView.as_view()),
    path('hotel-menus/', HotelMenuAPIView.as_view()),
    path('restourant-menus/', RestourantMenuAPIView.as_view()),
    path('cafe-menus/', CafeMenuAPIView.as_view())
]