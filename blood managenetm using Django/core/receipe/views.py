#import all libraries
from django.shortcuts import render, redirect 
from .models import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib.auth import logout


#login page for user
def login_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect('/login/')
            user_obj = authenticate(username=username, password=password)
            if user_obj:
                login(request, user_obj)
                return redirect('home')
            messages.error(request, "Wrong Password")
            return redirect('/login/')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register/')
    return render(request, "login.html")

#register page for user
def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect('/register/')
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Account created")
            return redirect('/login')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register')
    return render(request, "register.html")

#login page for admin
def login1(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect('/login1/')
            user_obj = authenticate(username=username, password=password)
            if user_obj:
                login(request, user_obj)
                return redirect('admin_home')
            messages.error(request, "Wrong Password")
            return redirect('/login1/')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/login1/')
    return render(request, "login1.html")


# database for patient
@login_required(login_url="/login/")
def bloods1(request):
    if request.method =='POST':
        data = request.POST
        blood1_status = data.get('blood1_status')
        blood1_fill = data.get('blood1_fill')
        blood1_age = data.get('blood1_age')
        blood1_reason = data.get('blood1_reason')
        blood1_name = data.get('blood1_name')
        blood1_description = data.get('blood1_description')
        Blood1.objects.create(
            blood1_status = blood1_status,
            blood1_fill = blood1_fill,
            blood1_age = blood1_age,
            blood1_reason= blood1_reason,
            blood1_name= blood1_name,
            blood1_description= blood1_description,
        )   
        return redirect('home')
    queryset = Blood1.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(blood1_name__icontains = request.GET.get('search'))        
        
    context = {'bloods1':queryset}
    return render(request, 'bloods1.html', context ) 

#delete data by admin
@login_required(login_url="/login1/")
def delete_blood1(request, id):
    queryset = Blood1.objects.get(id=id)
    queryset.delete()
    return redirect('admin_home')
    
   
#update data by admin 
@login_required(login_url="/login1/")
def update_blood1(request, id):
    queryset = Blood1.objects.get(id =id) 
    if  request.method == 'POST':
        data = request.POST   
        blood1_status = data.get('blood1_status')
        blood1_fill = data.get('blood1_fill')  
        blood1_age = data.get('blood1_age')  
        blood1_reason = data.get('blood1_reason')
        blood1_name = data.get('blood1_name')
        blood1_description = data.get('blood1_description')
        
        queryset.blood1_status = blood1_status
        queryset.blood1_fill = blood1_fill
        queryset.blood1_age = blood1_age
        queryset.blood1_reason = blood1_reason
        queryset.blood1_name = blood1_name
        queryset.blood1_description = blood1_description
         
           
        queryset.save()
        return redirect('admin_home')      
    context = {'blood1': queryset}
    return render(request, 'update_blood1.html', context)
    

#create data by donar
@login_required(login_url="/login/")
def bloods(request):
    if request.method =='POST':
        data = request.POST
        blood_status = data.get('blood_status')
        blood_age = data.get('blood_age')
        blood_fill = data.get('blood_fill')
        blood_date = data.get('blood_date')
        blood_name = data.get('blood_name')
        blood_description = data.get('blood_description')
        Blood.objects.create(
            blood_status = blood_status,
            blood_age = blood_age,
            blood_fill = blood_fill,
            blood_date= blood_date,
            blood_name= blood_name,
            blood_description= blood_description,
        )   
        return redirect('home')
    queryset = Blood.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(blood_name__icontains = request.GET.get('search'))        
        
    context = {'bloods':queryset}
    return render(request, 'bloods.html', context ) 


#delete data by admin
@login_required(login_url="/login1/")
def delete_blood(request, id):
    queryset = Blood.objects.get(id=id)
    queryset.delete()
    return redirect('/admin_home')
  
#update data by admin  
@login_required(login_url="/login1/")
def update_blood(request, id):
    queryset = Blood.objects.get(id =id) 
    if  request.method == 'POST':
        data = request.POST  
        blood_status = data.get('blood_status')
        blood_age = data.get('blood_age')
        blood_fill = data.get('blood_fill')     
        blood_date = data.get('blood_date')
        blood_name = data.get('blood_name')
        blood_description = data.get('blood_description')
         
        queryset.blood_status = blood_status
        queryset.blood_age = blood_age
        queryset.blood_fill = blood_fill
        queryset.blood_date = blood_date
        queryset.blood_name = blood_name
        queryset.blood_description = blood_description
           
        queryset.save()
        return redirect('admin_home')      
    context = {'blood': queryset}
    return render(request, 'update_blood.html', context)
    

#home page for user
@login_required(login_url="/login/")
def home(request):
    return render(request, 'home.html')


#request shown for patient
@login_required(login_url="/login/")
def request_me(request):
    if request.method =='POST':
        data = request.POST
        blood1_status = data.get('blood1_status')
        blood1_fill = data.get('blood1_fill')
        blood1_age  = data.get('blood1_age')
        blood1_reason = data.get('blood1_reason')
        blood1_name = data.get('blood1_name')
        blood1_description = data.get('blood1_description')
        Blood1.objects.create(
            blood1_status = blood1_status,
            blood1_age =blood1_age,
            blood1_fill = blood1_fill,
            blood1_reason= blood1_reason,
            blood1_name= blood1_name,
            blood1_description= blood1_description,
        )   
        return redirect('/first')
    queryset = Blood1.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(blood1_name__icontains = request.GET.get('search'))        
        
    context = {'bloods1':queryset}
    return render(request, 'request_me.html', context ) 


#request shown for donar
@login_required(login_url="/login/")
def request_u(request):
    if request.method =='POST':
        data = request.POST
        blood_status = data.get('blood_status')
        blood_age = data.get('blood_age')
        blood_fill = data.get('blood_fill')
        blood_date = data.get('blood_date')
        blood_name = data.get('blood_name')
        blood_description = data.get('blood_description')
        Blood.objects.create(
            blood_status = blood_status,
            blood_age = blood_age,
            blood_fill = blood_fill,
            blood_date= blood_date,
            blood_name= blood_name,
            blood_description= blood_description,
        )   
        return redirect('/request_u')
    queryset = Blood.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(blood_name__icontains = request.GET.get('search'))        
        
    context = {'bloods':queryset}
    return render(request, 'request_u.html', context ) 

#status updaation by admin
@login_required(login_url="/login1/")
def blood_need(request):
    if request.method =='POST':
        data = request.POST
        blood1_status = data.get('blood1_status')
        blood1_fill = data.get('blood1_fill')
        blood1_age = data.get('blood1_age')
        blood1_reason = data.get('blood1_reason')
        blood1_name = data.get('blood1_name')
        blood1_description = data.get('blood1_description')
        Blood1.objects.create(
            blood1_status = blood1_status,
            blood1_age = blood1_age,
            blood1_fill = blood1_fill,
            blood1_reason= blood1_reason,
            blood1_name= blood1_name,
            blood1_description= blood1_description,
        )   
        return redirect('admin_home')
    queryset = Blood1.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(blood1_name__icontains = request.GET.get('search'))        
        
    context = {'bloods1':queryset}
    return render(request, 'blood_need.html', context ) 

#request updation by admin
@login_required(login_url="/login1/")
def blood_offer(request):
    if request.method =='POST':
        data = request.POST
        blood_status = data.get('blood_status')
        blood_fill = data.get('blood_fill')
        blood_age = data.get('blood_age')
        blood_date = data.get('blood_date')
        blood_name = data.get('blood_name')
        blood_description = data.get('blood_description')
        Blood.objects.create( 
            blood_status = blood_status,
            blood_fill = blood_fill,
            blood_age = blood_age,
            blood_date= blood_date,
            blood_name= blood_name,
            blood_description= blood_description,
        )   
        return redirect('admin_home')
    queryset = Blood.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(blood_name__icontains = request.GET.get('search'))        
        
    context = {'bloods':queryset}
    return render(request, 'blood_offer.html', context ) 

#admin home page
@login_required(login_url="/login1/")
def admin_home(request):
    return render(request, 'admin_home.html')

#webisite main page
def main(request):
    return render(request, 'main.html')

#logout function
def custom_logout(request):
    logout(request)
    return redirect('main') 