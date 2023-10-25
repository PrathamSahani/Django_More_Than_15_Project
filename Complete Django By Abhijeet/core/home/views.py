from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    peoples = [
        {'name': 'Abhijeet', 'age':26},
        {'name': 'Rohan ', 'age':24},
        {'name': 'Om', 'age':21},
        {'name': 'Sandeep', 'age':29},
        
    ]
    
    for people in peoples:
        if people['age']:
            print("yes")
            
            
    vegitable = ['Pumpkin', 'Tomato', "Potato "]
    
     
    text = [ """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. A placeat maxime ad vel, nihil nisi repudiandae debitis
        ducimus eius pariatur incidunt dolor totam ullam quae repellendus quaerat sequi facere deserunt iusto magnam,
        consequatur ea. 
        
    """]
    
    return render(request, 'home/index.html', context ={'page': 'Django 2023' , 'peoples': peoples})


def about(request):
    context ={'page': 'About'}
    return render(request , "home/about.html", context)


def cotact(request):
    context ={'page': 'Contact'}
    return render(request, "home/contact.html", context)

def success(request):
    return HttpResponse("Hi this is the my success page")


