from rest_framework import serializers
from accounts.models import CustomUser
from app.models import *



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('__all__') 

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('__all__')
    
class RestourantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restourant
        fields = ('__all__')

class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = ('__all__')




class HotelMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelMenu
        fields = ('__all__')

class RestourantMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestourantMenu
        fields = ('__all__')

class CafeMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CafeMenu
        fields = ('__all__')