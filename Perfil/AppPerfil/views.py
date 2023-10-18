from django.shortcuts import render
from .models import Profile, UserInventory
from .serializers import ProfileSerializer,UserInventorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.db import transaction

class CreateProfile(APIView):
    def post(self,request):
        user = request.data.get('user')
        
        try:
            profile = Profile.objects.create(user=user)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except:
            return Response({'Error:':'Ya existe una cuenat asociada a este perfil'})

class ProfileView(APIView):
    def get(self,request,user):
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def post(self,request,user):
        game = request.data.get('games')
        subscription = request.data.get('sub')
        
        profile = Profile.objects.get(user=user)
        
        if subscription:
                if not profile.is_active_sub():
                    profile.activate_sub()
                    return Response({'Ok:':'Suscripcion activada exitosamente.'})
                else:
                    return Response({'Error:':'Ya tienes una suscripcion.'})
        else:
            profile.games += game
            profile.save()
            return Response({'Ok:':'Partidas agregadas'})
    
class UserInventoryView(APIView):
    def get(self,request,user):
        profile = UserInventory.objects.filter(user=user)
        serializer = UserInventorySerializer(profile,many=True)
        return Response(serializer.data)
    
class InventoryView(APIView):
    def get(self,request,user):
        profile = UserInventory.objects.filter(user=user)
        serializer = UserInventorySerializer(profile,many=True)
        return Response(serializer.data)

class AddInventary(APIView):
    def post(self,request):
        username = request.data.get('user')
        order_id = request.data.get('order_id')
        
        api_url = f'https://webserver.thenexusbattles2.cloud/obtener-orden/{order_id}'
        #api_url = f'http://localhost:3000/obtener-orden/{order_id}'
        response = requests.get(api_url)
        
        if response.status_code == 200:
            order_data = response.json()
            items = order_data.get('Items',[])
            with transaction.atomic():
                for item in items:
                    id_carta = item.get('id_carta')
                    
                    try:
                        card = UserInventory.objects.get(user=username,id_carta=id_carta)
                        card.quantity +=1
                        card.save()
                    except UserInventory.DoesNotExist:
                        response = requests.get('https://cards.thenexusbattles2.cloud/api/cartas/?size=50&page=1&coleccion=All&onlyActives=true')
                        data = response.json()
                        #iterar por el json
                        for carta in data:
                            #comparar el id del json con el id que pasamos
                            if carta.get('_id') == id_carta:
                                coleccion = carta.get('coleccion')
                        UserInventory.objects.create(user=username,id_carta=id_carta,type=coleccion)
                return Response({'Ok:':'Se almacenaron todos los cambios en el inventario'})
            