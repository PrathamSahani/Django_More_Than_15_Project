from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(['GET'])
def get_book(request):
    book_objs = Book.objects.all()
    serailizer = BookSerializer(book_objs, many=True)
    return Response({'status': 200, 'payload': serailizer.data})

