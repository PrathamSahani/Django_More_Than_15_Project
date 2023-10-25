from django.urls import path, include
from recipt import views

urlpatterns = [
    path('', views.index , name="home"),
    path('pdf/', views.gen_pdf, name='pdf'),
   
]
