
from django.urls import path, include
from .views import *



urlpatterns = [
    path('api/get', api, name = "api"),
    path('', home, name="home"),
]

