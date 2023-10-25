from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .helpers import *
from .models import User  # Make sure you import your User model

@api_view(['POST'])
def send_otp(request):
    data = request.data
    if data.get('phone_number') is None:
        return Response({
            'status': 400,
            'message': 'key phone_number is required'
        })

    if data.get('password') is None:
        return Response({
            'status': 400,
            'message': 'key password is required'
        })
    

    try:
        user = User.objects.create(
            phone_number=data.get('phone_number'),
            otp=send_otp_to_phone(data.get('phone_number'))
        )
        user.set_password(data.get('password'))
        user.save()

        return Response({
            'status': 200,
            'message': 'OTP sent'
        })
    except Exception as e:
        return Response({
            'status': 500,
            'message': 'An error occurred while creating the user'
        })


@api_view(['POST'])
def verify_otp(request):
    data = request.data

    if data.get('phone_number') is None:
        return Response({
            'status': 400,
            'message': 'key phone_number is required'
        })

    if data.get('otp') is None:
        return Response({
            'status': 400,
            'message': 'key otp is required'
        })

    try:
        user_obj = User.objects.get(phone_number=data.get('phone_number'))
    except User.DoesNotExist:
        return Response({
            'status': 400,
            'message': 'Invalid phone number'
        })

    if user_obj.otp == data.get('otp'):
        user_obj.is_phone_verified = True
        user_obj.save()
        return Response({
            'status': 200,
            'message': 'OTP matched'
        })
    else:
        return Response({
            'status': 400,
            'message': 'Invalid OTP'
        })
