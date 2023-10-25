from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home , name="home"),
    path('pdf/', views.gen_pdf, name='pdf'),
   
]
