from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
class Userserializer(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField(read_only = True)
    isAdmin = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = User
        fields = ['id','username','email','isAdmin']

    def get_isAdmin(self,obj):
        return obj.is_staff

    # def get_name(self,obj):
    #     name = obj.first_name
    #     return name
        

class userSerializerWithToken(Userserializer):
    token = serializers.SerializerMethodField(read_only = True)
    class Meta :
        model = User
        fields = ['id','username','email','isAdmin','token']
    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token)

class apiserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

