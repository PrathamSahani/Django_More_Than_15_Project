from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response



# Create your views here.


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        
        if not serializer.is_valid():
            # print(serializer.errors)
            return Response({'status': 403, 'errors': serializer.errors, 'message':"samoething went wrong"})
        
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token_obj , _= Token.objects.get_or_create(user=user)
        return Response({'status': 200, 'payload':serializer.data, 'token':str(token_obj), 'message': 'your data is saved'})