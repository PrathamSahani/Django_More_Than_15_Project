"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from receipe.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('logout/', custom_logout, name='logout'),
    
    path('login1/' , login1, name='login1'),
    
    path('login/' , login_page, name='login'),
    path('register/', register_page, name='register'),
    
    path('', main, name='main'),
    path('admin_home/', admin_home, name='admin_home'),
    
    path('blood_need/', blood_need, name='blood_need'),
    path('blood_offer/', blood_offer, name='blood_offer'),
    
    
    path('request_u/', request_u, name='request_u'),
    path('request_me/', request_me, name='request_me'),
    
    path('home/', home, name="home"),
    
    path("admin/", admin.site.urls),
    path('bloods' , bloods, name="bloods" ),
    path("delete_blood/<id>" , delete_blood, name="delete_blood"),
    path("update_blood/<id>" , update_blood, name="update_blood"),
    
    path('first/' , bloods1, name="first" ),
    path("delete_blood1/<id>" , delete_blood1, name="delete_blood1"),
    path("update_blood1/<id>" , update_blood1, name="update_blood1"),
]

if settings.DEBUG :
    urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()