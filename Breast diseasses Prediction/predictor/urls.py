from django.urls import path
from . import views

urlpatterns = [

    path('breast', views.breast, name="breast"),
    path('', views.home, name="home"),
]
