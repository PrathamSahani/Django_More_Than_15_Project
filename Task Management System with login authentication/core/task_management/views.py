from django.shortcuts import render, redirect
from .models import *  # Update the import to use the correct model name
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url="/login/")
def tasks(request):
    if request.method == 'POST':
        data = request.POST

        task_image = request.FILES.get('task_image')  # Correct the variable name
        task_name = data.get('task_name')  # Correct the variable name
        task_description = data.get('task_description')  # Correct the variable name

        Task.objects.create(
            task_image=task_image,  # Correct the field name
            task_name=task_name,  # Correct the field name
            task_description=task_description,  # Correct the field name
        )
        return redirect('/tasks/')

    queryset = Task.objects.all()  # Correct the model name

    if request.GET.get('search'):
        queryset = queryset.filter(task_name__icontains=request.GET.get('search'))  # Correct the field name

    context = {'tasks': queryset}  # Correct the variable name
    return render(request, 'task.html', context)


@login_required(login_url="/login/")
def delete_task(request, id):
    queryset = Task.objects.get(id=id)  # Correct the model name
    queryset.delete()
    return redirect('/tasks/')


@login_required(login_url="/login/")
def update_task(request, id):
    queryset = Task.objects.get(id=id)  # Correct the model name

    if request.method == 'POST':
        data = request.POST

        task_image = request.FILES.get('task_image')  # Correct the variable name
        task_name = data.get('task_name')  # Correct the variable name
        task_description = data.get('task_description')  # Correct the variable name

        queryset.task_name = task_name  # Correct the field name
        queryset.task_description = task_description  # Correct the field name

        if task_image:
            queryset.task_image = task_image  # Correct the field name

        queryset.save()
        return redirect('/tasks/')

    context = {'task': queryset}  # Correct the variable name
    return render(request, 'update_task.html', context)



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not  User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')       
        else:
            login(request, user)
            return redirect('/tasks/')
        
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    if request.method =='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(request, "Username already taken !")
            return redirect('/register/')
        
        
        user = User.objects.create_user(
            first_name = first_name, 
            last_name = last_name, 
            username = username
            
        )
        user.set_password(password)
        user.save()
        
        messages.info(request, "Account created Successfully !")
        return redirect('/register/')
        
    return render(request, 'register.html')
