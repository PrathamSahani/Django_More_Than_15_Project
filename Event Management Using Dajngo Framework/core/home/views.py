from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

@login_required(login_url="/login/")
def events(request):
    if request.method == 'POST':
        data = request.POST
        event_date = data.get('event_date')
        event_name = data.get('event_name')
        event_description = data.get('event_description')

        Events.objects.create(
            event_date=event_date,
            event_name=event_name,
            event_description=event_description,
        )
        return redirect('/')

    queryset = Events.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))

    context = {'events': queryset}
    return render(request, 'event.html', context)

@login_required(login_url="/login/")
def delete_event(request, id):
    queryset = Events.objects.get(id=id)
    queryset.delete()
    return redirect('/')

@login_required(login_url="/login/")
def update_event(request, id):
    queryset = Events.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        event_date = data.get('event_date')
        event_name = data.get('event_name')
        event_description = data.get('event_description')

        queryset.event_date = event_date
        queryset.event_name = event_name
        queryset.event_description = event_description

        queryset.save()
        return redirect('/')
    context = {'event': queryset}
    return render(request, 'update_event.html', context)

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
                return redirect('/')
            messages.error(request, "Wrong Password")
            return redirect('/login/')
        except Exception as e:
            messages.error(request, "Something went wrong")
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
            return redirect('/login')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register')
    return render(request, "register.html")

@login_required(login_url="/login/")
def update(request):
    if request.method == 'POST':
        data = request.POST
        event_date = data.get('event_date')
        event_name = data.get('event_name')
        event_description = data.get('event_description')

        Events.objects.create(
            event_date=event_date,
            event_name=event_name,
            event_description=event_description,
        )
        return redirect('/')

    queryset = Events.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))

    context = {'events': queryset}
    return render(request, 'update.html', context)

@login_required(login_url="/login/")
def show_event(request):
    if request.method == 'POST':
        data = request.POST
        event_date = data.get('event_date')
        event_name = data.get('event_name')
        event_description = data.get('event_description')

        Events.objects.create(
            event_date=event_date,
            event_name=event_name,
            event_description=event_description,
        )
        return redirect('/')

    queryset = Events.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))

    context = {'events': queryset}
    return render(request, 'show_event.html', context)
