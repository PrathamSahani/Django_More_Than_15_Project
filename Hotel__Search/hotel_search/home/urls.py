from .views import *
from django.urls import path, include 


urlpatterns = [
    path('' , home),
    path('api/get_hotels/', get_hotel ),
]    
