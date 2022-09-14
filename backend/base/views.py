from urllib import request
from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Product
from  .serializer import Userserializer, apiserializer,userSerializerWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response


# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer =  userSerializerWithToken(self.user).data 

        for k,v in serializer.items() :
            data[k] = v 

        return data
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserProfile (request):
    user = request.user

    serializer = Userserializer(user,many = False)
    return Response(serializer.data)





class api_views(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = apiserializer

class api_view_single(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    lookup_url_kwarg =  'id'
    serializer_class = apiserializer