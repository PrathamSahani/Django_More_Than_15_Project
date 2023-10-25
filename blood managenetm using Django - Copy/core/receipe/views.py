from django.shortcuts import render, redirect 
from .models import *
from django.http import HttpResponse


def receipes(request):
    if request.method =='POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        Receipe.objects.create(
            receipe_image= receipe_image,
            receipe_name= receipe_name,
            receipe_description= receipe_description,
        )   
        return redirect('first')
    queryset = Receipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))        
        
    context = {'receipes':queryset}
    return render(request, 'receipes.html', context ) 

def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('first')
    
def update_receipe(request, id):
    queryset = Receipe.objects.get(id =id) 
    if  request.method == 'POST':
        data = request.POST       
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        
        if receipe_image :
            queryset.receipe_image = receipe_image         
           
        queryset.save()
        return redirect('first')      
    context = {'receipe': queryset}
    return render(request, 'update_receipe.html', context)
    



def bloods(request):
    if request.method =='POST':
        data = request.POST
        blood_image = request.FILES.get('blood_image')
        blood_name = data.get('blood_name')
        blood_description = data.get('blood_description')
        Blood.objects.create(
            blood_image= blood_image,
            blood_name= blood_name,
            blood_description= blood_description,
        )   
        return redirect('/bloods')
    queryset = Blood.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(blood_name__icontains = request.GET.get('search'))        
        
    context = {'bloods':queryset}
    return render(request, 'bloods.html', context ) 

def delete_blood(request, id):
    queryset = Blood.objects.get(id=id)
    queryset.delete()
    return redirect('/bloods')
    
def update_blood(request, id):
    queryset = Blood.objects.get(id =id) 
    if  request.method == 'POST':
        data = request.POST       
        blood_image = request.FILES.get('blood_image')
        blood_name = data.get('blood_name')
        blood_description = data.get('blood_description')
        
        queryset.blood_name = blood_name
        queryset.blood_description = blood_description
        
        if blood_image :
            queryset.blood_image = blood_image         
           
        queryset.save()
        return redirect('/bloods')      
    context = {'blood': queryset}
    return render(request, 'update_blood.html', context)
    


def home(request):
    return render(request, 'home.html')



def request_me(request):
    if request.method =='POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        Receipe.objects.create(
            receipe_image= receipe_image,
            receipe_name= receipe_name,
            receipe_description= receipe_description,
        )   
        return redirect('/first')
    queryset = Receipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))        
        
    context = {'receipes':queryset}
    return render(request, 'request_me.html', context ) 



def request_u(request):
    if request.method =='POST':
        data = request.POST
        blood_image = request.FILES.get('blood_image')
        blood_name = data.get('blood_name')
        blood_description = data.get('blood_description')
        Blood.objects.create(
            blood_image= blood_image,
            blood_name= blood_name,
            blood_description= blood_description,
        )   
        return redirect('/request_u')
    queryset = Blood.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(blood_name__icontains = request.GET.get('search'))        
        
    context = {'bloods':queryset}
    return render(request, 'request_u.html', context ) 




def blood_need(request):
    if request.method =='POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        Receipe.objects.create(
            receipe_image= receipe_image,
            receipe_name= receipe_name,
            receipe_description= receipe_description,
        )   
        return redirect('first')
    queryset = Receipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))        
        
    context = {'receipes':queryset}
    return render(request, 'blood_need.html', context ) 



def blood_offer(request):
    if request.method =='POST':
        data = request.POST
        blood_image = request.FILES.get('blood_image')
        blood_name = data.get('blood_name')
        blood_description = data.get('blood_description')
        Blood.objects.create(
            blood_image= blood_image,
            blood_name= blood_name,
            blood_description= blood_description,
        )   
        return redirect('/blood_offer')
    queryset = Blood.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(blood_name__icontains = request.GET.get('search'))        
        
    context = {'bloods':queryset}
    return render(request, 'blood_offer.html', context ) 


def admin_home(request):
    return render(request, 'admin_home.html')


def main(request):
    return render(request, 'main.html')