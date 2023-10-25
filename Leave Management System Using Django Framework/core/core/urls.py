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

#import all libraries
from django.contrib import admin
from django.urls import path
from home.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


#urlpattern join all url
urlpatterns = [
    path('', main, name="main"),
    path('admin_home', admin_home, name="admin_home"),
    path('login1/', login1, name="login1"),
    path('show_leave/', show_leave, name="show_leave"),
    path('update/', update, name="update"),
    path("admin/", admin.site.urls),
    path("leaves/", leaves, name="leaves" ),
    path('main' , home , name="home"),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path("delete_leave/<id>" , delete_leave, name="delete_leave"),
    path("update_leave/<id>" , update_leave, name="update_leave"),
]

#static file method 
if settings.DEBUG :
    urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()