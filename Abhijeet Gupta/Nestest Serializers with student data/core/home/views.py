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
    
    
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializers(student_objs, many = True)
        print(request.user)
        return Response({'status': 200, 'payload': serializer.data})
    
    def post(self, request):
       serializer = StudentSerializers(data = request.data)
       
       if not serializer.is_valid():
           print(serializer.errors)
           return Response({'status': 403, 'errors':serializer.errors, 'message':'Something went wrong '})
       
       serializer.save()
       return Response({'status': 200, 'payload': serializer.data, 'messge': 'your data is saved'})
   
       
    def put(self, request):
        try:
            student_obj = Student.objects.get(id = request.data['id'])
            serializer = StudentSerializers(student_obj, data = request.data)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'errors':serializer.errors, 'messge':'Something went wrong'})
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message':'your data is updated'})
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'Invalid id'})
    
    
    def patch(self, request):
        try:
            student_obj = Student.objects.get(id = request.data['id'])
            serializer = StudentSerializers(student_obj, data = request.data, partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'errors':serializer.errors, 'messge':'Something went wrong'})
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message':'your data is updated'})
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'Invalid id'})
    
    
    
    
    
    
    def delete(self, request):
        try:
            id = request.GET.get('id')
            student_obj = Student.objects.get(id =id)
            student_obj.delete()
            return Response({'status': 200, 'massage': 'deleted'})
        except Exception as e:
            print(e)
            return Response({'status': 403, 'massage': 'Invalid id'})
        




# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serailizer = StudentSerializers(student_objs, many= True)
#     return Response({'status': 200, 'payload': serailizer.data})

# @api_view(['POST'])
# def post_student(request):
#     data= request.data
#     serializer = StudentSerializers(data = request.data)
    
    
    
#     if not serializer.is_valid():
#         print(serializer.errors)
#         return Response({'status': 403, 'errors': serializer.errors , 'messge':"Something went wrong"})
    
#     serializer.save()
        
#     return Response({'status' : 200, 'payload': serializer.data, 'messge':'you data is saved '})


# @api_view(['PUT'])
# def update_student(request, id):
#     try:
#         student_obj = Student.objects.get(id = id)
#         serializer = StudentSerializers(student_obj, data = request.data, partial=True )
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status': 403, 'errors':serializer.errors, 'mesge':'Something went wrong'})
        
#         serializer.save()
#         return Response({'status': 200, 'payload': serializer.data, 'messge':'you data is saved'})
    
#     except Exception as e:
#         print(e)
#         return Response({'status': 403, 'messge':'invalid id'})
    
    

# @api_view(['PATCH'])
# def update_student(request, id):
#     try:
#         student_obj = Student.objects.get(id = id)
#         serializer = StudentSerializers(student_obj, data = request.data, partial=True )
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status': 403, 'errors':serializer.errors, 'mesge':'Something went wrong'})
        
#         serializer.save()
#         return Response({'status': 200, 'payload': serializer.data, 'messge':'you data is saved'})
    
#     except Exception as e:
#         print(e)
#         return Response({'status': 403, 'messge':'invalid id'})
    
    
# @api_view(['DELETE'])
# def delete_student(request, id):
#     try:
#         # id = request.GET.get('id')
#         student_obj = Student.objects.get(id = id)
#         student_obj.delete()
#         return Response({'status': 200 , 'massage': 'deleted'})
    
    
        
#     except Exception as e:
#         print(e)
#         return Response({'status':403, 'massage':'Data is saved'})