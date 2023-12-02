from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Cliente

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserSerializer, ClienteSerializer

# Create your views here.

class UserList(APIView):
    def post(self, request, **kwards):
        print(request)
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

class UserDetails(APIView): #Fijarse como no devolver la contraseña
    def get(self, request, pk, **kwards):
        user = User.objects.filter( id=pk).first()
        serializer = UserSerializer(user)

        if user is not None:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("{error: WRONG pk}", status=status.HTTP_400_BAD_REQUEST)
