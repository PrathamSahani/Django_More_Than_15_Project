#import all libraries
from django.shortcuts import render, redirect 
from .models import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

#Create home page
def home(request):
    return render(request, 'home.html')

#Main home page
def main(request):
    return render(request, 'main.html')

#admin_home page
def admin_home(request):
    return render(request, 'admin_home.html')

#Create leave page
@login_required(login_url="/login/")
def leaves(request):
    if request.method =='POST':
        data = request.POST
        
        leave_accept = data.get('leave_accept')
        leave_date = data.get('leave_date')
        name = data.get('name')
        leave_description = data.get('leave_description')    
        Leaves.objects.create(
            
            leave_accept= leave_accept,
            leave_date= leave_date,
            name= name,
            leave_description= leave_description,
        )   
        return redirect('/main')
    
    queryset = Leaves.objects.all() 
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))       
        
    context = {'leaves':queryset}
    return render(request, 'leave.html', context ) 


#Delete the leave 
@login_required(login_url="/login/")
def delete_leave(request, id):
    queryset = Leaves.objects.get(id=id)
    queryset.delete()
    return redirect('main')

#Update the leave 
@login_required(login_url="/login/")
def update_leave(request, id):
    # Use get_object_or_404 to handle the case when the record doesn't exist
    queryset = Leaves.objects.get(id=id)

    if request.method == 'POST':
        # Use request.POST.get() to safely retrieve form data
        leave_accept = request.POST.get('leave_accept')
        leave_date = request.POST.get('leave_date')
        name = request.POST.get('name')
        leave_description = request.POST.get('leave_description')

        # Update the model fields
        queryset.leave_accept = leave_accept
        queryset.leave_date = leave_date
        queryset.name = name
        queryset.leave_description = leave_description

        # Save the updated object
        queryset.save()
        return redirect('admin_home')
 
    context = {'leave': queryset}
    return render(request, 'update_leave.html', context)
    

#Login Page
def login_page(request):
    if request.method == "POST":
        
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect('/login/')
            user_obj = authenticate(username=username, password = password)
            if user_obj:
                login(request, user_obj)
                return redirect('/main')
            messages.error(request, "Wrong Password")
            return redirect('/login/')
            
        except Exception as e:
            messages.error(request, " Somthing went wrong")
            return redirect('/register/')
        
    return render(request, "login.html")


#Register page function
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
            return redirect('/login/')

        except Exception as e:
            messages.error(request, " Somthing went wrong")
            return redirect('/register/')
 
    return render(request, "register.html")


#Update the page
@login_required(login_url="/login1/")
def update(request):
    if request.method =='POST':
        data = request.POST
        
        leave_accept = data.get('leave_accept')
        leave_date = data.get('leave_date')
        name = data.get('name')
        leave_description = data.get('leave_description')
        
        Leaves.objects.create(
            leave_accept = leave_accept,
            leave_date= leave_date,
            name= name,
            leave_description= leave_description,
        )   
        return redirect('admin_home')
    
    
    queryset = Leaves.objects.all()  
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
        
    context = {'leaves':queryset}
    return render(request, 'update.html', context ) 


#Shown all data
@login_required(login_url="/login/")
def show_leave(request):
    if request.method =='POST':
        data = request.POST
        
        leave_accept = data.get('leave_accept')
        leave_date = data.get('leave_date')
        name = data.get('name')
        leave_description = data.get('leave_description')      
        Leaves.objects.create(
            leave_date= leave_date,
            name= name,
            leave_description= leave_description,
        )   
        return redirect('/main')
    
    
    queryset = Leaves.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))      
        
    context = {'leaves':queryset}
    return render(request, 'show_leave.html', context )


#Admin login page
def login1(request):
    if request.method == "POST":
        
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect('/login1/')
            user_obj = authenticate(username=username, password = password)
            if user_obj:
                login(request, user_obj)
                return redirect('/admin_home')
            messages.error(request, "Wrong Password")
            return redirect('/login1/')
            
        except Exception as e:
            messages.error(request, " Somthing went wrong")
            return redirect('/login1/')
        
    return render(request, "login1.html")


