from django.urls import path
from .views import *

urlpatterns = [
    path('', UsersListView, name='home'),
    path('create/hotel/', HotelCreateView.as_view(), name='create-hotel'),
    path('create/restourant/', RestourantCreateView.as_view(), name='create-restourant'),
    path('create/cafe/', CafeCreateView.as_view(), name='create-cafe'),
    path('detail/hotel/<int:id>/', HotelDetailView, name='detail-hotel'),
    path('detail/restourant/<int:id>/', RestourantDetailView, name='detail-restourant'),
    path('detail/cafe/<int:id>/', CafeDetailView, name='detail-cafe'),
    path('create/hotel/menu/', CreateHotelMenuView, name='create-hotel-menu'),
    path('create/restourant/menu/', CreateRestourantMenuView, name='create-restourant-menu'),
    path('create/cafe/menu/', CreateCafeMenuView, name='create-cafe-menu'),
]