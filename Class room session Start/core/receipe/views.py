from django.shortcuts import render, redirect 
from .models import *
from django.http import HttpResponse


def receipes(request):
    if request.method =='POST':
        data = request.POST  
        receipe_link = data.get('receipe_link')
        # receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        
        Receipe.objects.create(
            receipe_link= receipe_link,
            receipe_name= receipe_name,
            receipe_description= receipe_description,
        )   
        return redirect('show')
    
    
    queryset = Receipe.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
        
        
        
    context = {'receipes':queryset}
    return render(request, 'receipes.html', context )


def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('show')


    
def update_receipe(request, id):
    queryset = Receipe.objects.get(id =id)
    
    if  request.method == 'POST':
        data = request.POST
        
        receipe_link = data.get('receipe_link')
        # receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        queryset.receipe_link = receipe_link       
           
        queryset.save()
        return redirect('show')      
    context = {'receipe': queryset}
    return render(request, 'update_receipe.html', context)


def show(request):
    if request.method =='POST':
        data = request.POST  
        receipe_link = data.get('receipe_link')
        # receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        
        Receipe.objects.create(
            receipe_link= receipe_link,
            receipe_name= receipe_name,
            receipe_description= receipe_description,
        )   
        return redirect('show')
    
    
    queryset = Receipe.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
        
        
        
    context = {'receipes':queryset}
    return render(request, 'show.html', context ) 

def classes(request):
    if request.method =='POST':
        data = request.POST  
        receipe_link = data.get('receipe_link')
        # receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        
        Receipe.objects.create(
            receipe_link= receipe_link,
            receipe_name= receipe_name,
            receipe_description= receipe_description,
        )   
        return redirect('show')
    
    
    queryset = Receipe.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
        
        
        
    context = {'receipes':queryset}
    return render(request, 'class.html', context ) 

