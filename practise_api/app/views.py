from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from accounts.models import CustomUser
from .models import *
from urllib import request

def UsersListView(request):
    user_lists = CustomUser.objects.all()
    hotel_lists = Hotel.objects.all()
    restourant_lists = Restourant.objects.all()
    cafe_lists = Cafe.objects.all()
    return render(request, 'html/index.html', context={'user_lists': user_lists, 'hotel_lists': hotel_lists, 'restourant_lists': restourant_lists, 'cafe_lists': cafe_lists})

class HotelCreateView(CreateView):
    model = Hotel
    template_name = 'html/create_hotel.html'
    fields = ('name', 'rate', 'about', 'adress', 'photo1', 'photo2', 'photo3', 'cost', 'ig', 'tg', 'phone_num')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RestourantCreateView(CreateView):
    model = Restourant
    template_name = 'html/create_restourant.html'
    fields = ('name', 'about', 'rate', 'adress', 'photo1', 'photo2', 'photo3', 'cost', 'phone_num', 'ig', 'tg', 'dostavka')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CafeCreateView(CreateView):
    model = Cafe
    fields = ('name', 'about', 'rate', 'adress', 'photo1', 'photo2', 'photo3', 'cost', 'phone_num', 'ig', 'tg')
    template_name = 'html/create_cafe.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def HotelDetailView(request, id):
    obj = Hotel.objects.get(id=id)
    return render(request, 'html/hotel_detail.html', context={'obj': obj})

def RestourantDetailView(request, id):
    obj = Restourant.objects.get(id=id)
    return render(request, 'html/restourant_detail.html', context={'obj': obj})

def CafeDetailView(request, id):
    obj = Cafe.objects.get(id=id)
    return render(request, 'html/cafe_detail.html', context={'obj':obj})

def CreateHotelMenuView(request):
    if request.method == "POST":
        hotel_id = request.POST['hotel_id']
        food_name = request.POST['food_name']
        price = request.POST['price']
        category = request.POST['category']
    hotel = Hotel.objects.get(id=hotel_id)
    HotelMenu.objects.create(hotel=hotel, food_name=food_name, price=price, category=category)
    return redirect('detail-hotel', id=hotel_id)

def CreateRestourantMenuView(request):
    if request.method == "POST":
        restourant_id = request.POST['restourant_id']
        food_name = request.POST['food_name']
        price = request.POST['price']
        category = request.POST['category']
    restourant = Restourant.objects.get(id=restourant_id)
    RestourantMenu.objects.create(restourant=restourant, food_name=food_name, price=price, category=category)
    return redirect('detail-restourant', id=restourant_id)

def CreateCafeMenuView(request):
    if request.method == "POST":
        cafe_id = request.POST['cafe_id']
        food_name = request.POST['food_name']
        price = request.POST['price']
        category = request.POST['category']
    cafe = Cafe.objects.get(id=cafe_id)
    CafeMenu.objects.create(cafe=cafe, food_name=food_name, price=price, category=category)
    return redirect('detail-cafe', id=cafe_id)
    
