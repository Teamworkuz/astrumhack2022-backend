from django.urls import *
from .views import *

urlpatterns = [
    path('create_user/', CustomUserCreateView.as_view(), name='create-user')
]