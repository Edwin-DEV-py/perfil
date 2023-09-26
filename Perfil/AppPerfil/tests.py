from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Profile, UserInventory
from .serializers import ProfileSerializer, UserInventorySerializer


#Prueba #1: Perfil

class ProfileViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        #Perfil de prueba
        self.user = 'usuario_prueba'
        self.profile = Profile.objects.create(user=self.user, games=10, sub=False)

    def test_get_profile(self):
        #URL
        url = reverse('perfil', args=[self.user])

        #Get
        response = self.client.get(url, format='json')

        #Verificar que la respuesta sea un 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('Prueba para ver el perfil del usuario')
        print(response.data)
        print('--------------------------------------------------')
        
    def test_get_no_profile(self):
        # Usuario inexistente en la base de datos
        non_existent_user = 'usuario_inexistente'

        #URL
        url = reverse('perfil', args=[non_existent_user])

        #Get
        try:
            response = self.client.get(url, format='json')
            
            # Verificar que la respuesta sea un 404 Not Found
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
            print('Prueba para ver si no existe el perfil')
            print(response.data)
            print('--------------------------------------------------')
        except Profile.DoesNotExist:
            print('No existe el perfil')
            print('--------------------------------------------------')
            
class InventoryViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        #Crear un inventario
        self.user = 'usuario_prueba'
        self.inventory = UserInventory.objects.create(user=self.user, id_carta='CartaPrueba', quantity=1)

    def test_get_user_inventory(self):
        #URL
        url = reverse('inventario', args=[self.user])

        #GET
        response = self.client.get(url, format='json')

        # Verificar que la respuesta sea un 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('Prueba para ver el inventario del usuario')
        print(response.data)
        print('--------------------------------------------------')