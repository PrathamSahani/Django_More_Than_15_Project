from django.shortcuts import render
from django.http import JsonResponse
from .models import Restro
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

# Create your views here.

def home(request):
    return render(request, "home.html")

def api(request):
    restro_objs = Restro.objects.all()
    pincode = request.GET.get('pincode')
    # print(pincode)
    km  = request.GET.get('km')
    
    user_lat = None
    user_long = None
    if pincode :
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(int(pincode))
        user_lat = location.latitude  # Corrected 'locaton' to 'location'
        user_long = location.longitude
        
        
    
    payload = []
    
    for restro_obj in restro_objs:
        result = {}
        result['name'] = restro_obj.name
        result['image'] = restro_obj.image
        result['description'] = restro_obj.description
        result['pincode'] = restro_obj.pincode
        if pincode :
            frist = (float(user_lat), float(user_long))
            second = (float(restro_obj.lat), float(restro_obj.lon))
            result['distance'] = int(great_circle(frist, second).miles)
        
        payload.append(result)
        if km:
            if result['distance'] > int(km):
                payload.pop()
      
        
    return JsonResponse(payload, safe=False)
