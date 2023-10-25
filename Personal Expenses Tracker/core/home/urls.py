
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('', home , name="home"),
   
]
