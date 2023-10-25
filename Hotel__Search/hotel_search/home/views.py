# Import necessary modules and models
from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Define the 'home' view function
def home(request):
    # Return the 'home.html' template when the home page is accessed
    return render(request, 'home.html')

# Define the 'get_hotel' view function
def get_hotel(request):
    try:
        # Get all hotel objects from the database
        hotel_objs = Hotel.objects.all()

        # Check if the 'sort_by' parameter is present in the GET request
        if request.GET.get('sort_by'):
            sort_by_value = request.GET.get('sort_by')
            # If 'sort_by' is 'asc', order hotels by price in ascending order
            if sort_by_value == 'asc':
                hotel_objs = hotel_objs.order_by('hotel_price')
            # If 'sort_by' is 'dsc', order hotels by price in descending order
            elif sort_by_value == 'dsc':
                hotel_objs = hotel_objs.order_by('-hotel_price')

            # Check if the 'amount' parameter is also present in the GET request
            if request.GET.get('amount'):
                amount = request.GET.get('amount')
                # Filter hotels by price, showing only those with a price less than or equal to 'amount'
                hotel_objs = hotel_objs.filter(hotel_price__lte=amount)

        # Create an empty list to store hotel information
        payload = []
        
        # Iterate through the hotel objects and add their details to the payload list
        for hotel_obj in hotel_objs:
            payload.append({
                'hotel_name': hotel_obj.hotel_name,
                'hotel_price': hotel_obj.hotel_price,
                'hotel_description': hotel_obj.hotel_description,
            })

        # Return the hotel information as JSON response
        return JsonResponse(payload, safe=False)

    except Exception as e:
        # Handle any exceptions and print an error message
        print(e)

    # Return a JSON response with an error message if something goes wrong
    return JsonResponse({'message': 'Something went wrong!'})
