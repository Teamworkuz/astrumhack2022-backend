from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_displays = ['username', 'email', 'fish', 'phone_number']

admin.site.register(CustomUser, CustomUserAdmin)
