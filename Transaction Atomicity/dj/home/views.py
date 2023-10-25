from django.shortcuts import render
from django.contrib import messages
from .models import Payment  # Import the Payment model from your models.py file
from django.db import transaction


def home(request):
    if request.method == 'POST':
        try:
            user_one = request.POST.get('user_one')
            user_two = request.POST.get('user_two')
            amount = int(request.POST.get('amount'))  # Convert the amount to an integer
            with transaction.atomic():
                user_one_payment_obj = Payment.objects.get(user=user_one)  # Fix the model name
                user_two_payment_obj = Payment.objects.get(user=user_two)  # Fix the model name
                    
                user_one_payment_obj.amount -= amount  # Fix the subtraction operation
                user_one_payment_obj.save()
                    
                user_two_payment_obj.amount += amount  # Fix the addition operation
                user_two_payment_obj.save()
            
           
            messages.success(request, "Amount transferred successfully")  # Add 'request' as the first argument
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    
    return render(request, 'home.html')
