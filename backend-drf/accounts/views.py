from django.shortcuts import render
from accounts.serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] 


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    

    def get(self , request):
        respone = {
            'status':'request was permitted'
        }

        return Response(respone)



    