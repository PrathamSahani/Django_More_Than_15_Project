from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('api/hotels', api_hotels ),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
 
    
]
