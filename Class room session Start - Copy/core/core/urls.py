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
    path('', select, name = 'select'),
    path('class/', classes , name ='class'),
    path("admin/", admin.site.urls),
    path("show/", show, name='show'),
    path('subjects/' , subjects , name ="create_class"),
    path('student_home/', student_home, name = "student_home"),
    path('teacher_home/', teacher_home, name = "teacher_home"),
    path('logins/', login_pages, name="logins"),
    path('registers/', register_pages, name="registers"),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path("delete_subject/<id>" , delete_subject, name="delete_subject"),
    path("update_subject/<id>" , update_subject, name="update_subject"),
]

if settings.DEBUG :
    urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()