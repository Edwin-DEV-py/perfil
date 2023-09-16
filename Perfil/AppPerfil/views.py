from django.shortcuts import render
from .models import Profile, UserInventory
from .serializers import ProfileSerializer,UserInventorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class ProfileView(APIView):
    def get(self,request,user):
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
class UserInventoryView(APIView):
    def get(self,request,user):
        profile = UserInventory.objects.filter(user=user)
        serializer = UserInventorySerializer(profile,many=True)
        return Response(serializer.data)
