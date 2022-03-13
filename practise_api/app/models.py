from random import choices
from django.db import models
from django.urls import reverse_lazy

RATE_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)

CHANCE_CHOICES = (
    ('NETWORK', 'Network'),
    ('EAT', 'Eat'),
    ('SWIM', 'Swim'),
    ('FITNESS', 'Fitness')
)

STATUS_CHOICES = (
    ('ACTIVE', 'Activ'),
    ('NOT_ACTIVE', 'Not_Active')
)

DOSTAVKA_CHOICES = (
    ('BOR', 'Bor'),
    ("YO'Q", "Yo'q")
)

CATEGORY_CHOICES = (
    ('HOTEL', 'Hotel'),
    ('RESTOURANT', 'Restourant'),
    ('CAFE', 'Cafe')
)

FOOD_CHOICES = (
    ('YEVROPACHA', 'Yevropacha'),
    ('OSIYOCHA', 'Osiyocha')
)

class Hotel(models.Model):
    type = models.CharField(choices=CATEGORY_CHOICES, max_length=50, default='Hotel')
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    about = models.TextField(null=True)
    rate = models.CharField(choices=RATE_CHOICES, max_length=50)
    adress = models.CharField(max_length=100)
    photo1 = models.ImageField(upload_to='hotel_photos/')
    photo2 = models.ImageField(upload_to='re_photos/')
    photo3 = models.ImageField(upload_to='cafe_photos/')
    cost = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='Active')
    ig = models.CharField(max_length=100, null=True)
    tg = models.CharField(max_length=100, null=True)
    phone_num = models.BigIntegerField(null=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('home')

class Restourant(models.Model):
    type = models.CharField(choices=CATEGORY_CHOICES, max_length=50, default='Restourant')
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    about = models.TextField(null=True)
    rate = models.CharField(choices=RATE_CHOICES, max_length=50)
    adress = models.CharField(max_length=100)
    photo1 = models.ImageField(upload_to='hotel_photos/')
    photo2 = models.ImageField(upload_to='re_photos/')
    photo3 = models.ImageField(upload_to='cafe_photos/')
    cost = models.IntegerField(default=0)
    phone_num = models.BigIntegerField(null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='Active')
    ig = models.CharField(max_length=100, null=True)
    tg = models.CharField(max_length=100, null=True)
    dostavka = models.CharField(choices=DOSTAVKA_CHOICES, max_length=50, default='Bor')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('home')
    
class Cafe(models.Model):
    type = models.CharField(choices=CATEGORY_CHOICES, max_length=50, default='Cafe')
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    about = models.TextField(null=True)
    rate = models.CharField(choices=RATE_CHOICES, max_length=50)
    adress = models.CharField(max_length=100)
    photo1 = models.ImageField(upload_to='hotel_photos/')
    photo2 = models.ImageField(upload_to='re_photos/')
    photo3 = models.ImageField(upload_to='cafe_photos/')
    cost = models.IntegerField(default=0)
    phone_num = models.BigIntegerField(null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='Active')
    ig = models.CharField(max_length=100, null=True)
    tg = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('home')

class HotelMenu(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotelmenu',null=True)
    food_name = models.CharField(max_length=100)
    category = models.CharField(choices=FOOD_CHOICES, max_length=50)
    price = models.IntegerField()
    
    def __str__(self):
        return f'{self.hotel} - {self.food_name}'
    

class RestourantMenu(models.Model):
    restourant = models.ForeignKey(Restourant, on_delete=models.CASCADE, related_name='restourantmenu', null=True)
    food_name = models.CharField(max_length=100)
    category = models.CharField(choices=FOOD_CHOICES, max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.restourant} - {self.food_name}'

class CafeMenu(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='cafemenu', null=True)
    food_name = models.CharField(max_length=100)
    category = models.CharField(choices=FOOD_CHOICES, max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.cafe} - {self.food_name}'


    