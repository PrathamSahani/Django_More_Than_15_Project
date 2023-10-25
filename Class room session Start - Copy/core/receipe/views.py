from django.shortcuts import render, redirect 
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def select(request):
    return render(request, 'select.html')

@login_required(login_url="/login/")
def subjects(request):
    if request.method =='POST':
        data = request.POST  
        class_link = data.get('class_link')
        subject_name = data.get('subject_name')
        subject_description = data.get('subject_description')
        
        Shedule.objects.create(
            class_link= class_link,
            subject_name= subject_name,
            subject_description= subject_description,
        )   
        return redirect('show')
    
    
    queryset = Shedule.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(subject_name__icontains = request.GET.get('search'))
             
    context = {'subjects':queryset}
    return render(request, 'shedule.html', context )

@login_required(login_url="/login/")
def delete_subject(request, id):
    queryset = Shedule.objects.get(id=id)
    queryset.delete()
    return redirect('show')


@login_required(login_url="/login/")  
def update_subject(request, id):
    queryset = Shedule.objects.get(id =id)
    
    if  request.method == 'POST':
        data = request.POST
        
        class_link = data.get('class_link')
        subject_name = data.get('subject_name')
        subject_description = data.get('subject_description')
        
        queryset.subject_name = subject_name
        queryset.subject_description = subject_description
        queryset.class_link = class_link       
           
        queryset.save()
        return redirect('show')      
    context = {'subject': queryset}
    return render(request, 'update_shedule.html', context)


@login_required(login_url="/login/")
def show(request):
    if request.method =='POST':
        data = request.POST  
        class_link = data.get('class_link')
        subject_name = data.get('subject_name')
        subject_description = data.get('subject_description')
        
        Shedule.objects.create(
            class_link= class_link,
            subject_name= subject_name,
            subject_description= subject_description,
        )   
        return redirect('show')
    
    queryset = Shedule.objects.all() 
    if request.GET.get('search'):
        queryset = queryset.filter(subject_name__icontains = request.GET.get('search'))
        
    context = {'subjects':queryset}
    return render(request, 'show.html', context ) 

@login_required(login_url="/login/")
def classes(request):
    if request.method =='POST':
        data = request.POST  
        class_link = data.get('class_link')
        subject_name = data.get('subject_name')
        subject_description = data.get('subject_description')
        
        Shedule.objects.create(
            class_link= class_link,
            subject_name= subject_name,
            subject_description= subject_description,
        )   
        return redirect('show')
       
    queryset = Shedule.objects.all()  
    if request.GET.get('search'):
        queryset = queryset.filter(subject_name__icontains = request.GET.get('search'))
               
    context = {'subjects':queryset}
    return render(request, 'class.html', context ) 

@login_required(login_url="/login/")
def student_home(request):
    return render(request, 'student_home.html')

@login_required(login_url="/login/")
def teacher_home(request):
    return render(request, 'teacher_home.html')


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
                return redirect('student_home')
            messages.error(request, "Wrong Password")
            return redirect('/login/')
            
        except Exception as e:
            messages.error(request, " Somthing went wrong")
            return redirect('/register/')
        
    return render(request, "login.html")

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


def login_pages(request):
    if request.method == "POST":
        
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect('/logins/')
            user_obj = authenticate(username=username, password = password)
            if user_obj:
                login(request, user_obj)
                return redirect('teacher_home')
            messages.error(request, "Wrong Password")
            return redirect('/logins/')
            
        except Exception as e:
            messages.error(request, " Somthing went wrong")
            return redirect('/registers/')
        
    return render(request, "login1.html")



def register_pages(request):
    if request.method == "POST":      
        try:          
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect('/registers/')
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Account created")
            return redirect('/logins/')
        except Exception as e:
            messages.error(request, " Somthing went wrong")
            return redirect('/registers/')       
        
    return render(request, "register1.html")