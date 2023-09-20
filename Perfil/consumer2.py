import os
import django
import requests
from django.db import transaction
#obtener las configuraciones del settings para poder ejecutar este archivo
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Perfil.settings')
django.setup()

import pika, json
from AppPerfil.models import UserInventory

#conectar con cloudAMQP
params = pika.URLParameters('amqps://pimhdfyz:v79_lwTMTMNkSRg3qgGxbQC1nD2y6ivM@jaragua.lmq.cloudamqp.com/pimhdfyz')
connection = pika.BlockingConnection(params)
channel = connection.channel()
print('conectado2')
#definir el canal
channel.queue_declare(queue='perfil',durable=True)#anadir durable=True para que los mensaje lleguen a pesar de que este apagado
#implementa el protocolo de mensajeria AMQP para declarar una cola.
#una cola es un destino donde los productores envian mensajes y los consumidores reciben. este protocolo crea una cola.

#funcion para saber que obtuvo los datos
def callback(ch, method,properties, body):
    print('resibido en perfil')
    
    data = json.loads(body)
    
    if properties.content_type == 'agregar-perfil':
        username = data['user']
        order_id = data['order_id']
        
        api_url = f'https://store.thenexusbattles2.cloud/webserver/obtener-orden/66'
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
                        response = requests.get('https://cards.thenexusbattles2.cloud/api/all/')
                        data = response.json()
                        #iterar por el json
                        for carta in data:
                            #comparar el id del json con el id que pasamos
                            if carta.get('_id') == id_carta:
                                coleccion = carta.get('coleccion')
                        UserInventory.objects.create(user=username,id_carta=id_carta,type=coleccion)
                        print('Carta guardada')
        print('Se anadieron todas las cartas al perfil')
        
        
channel.basic_consume(queue='perfil', on_message_callback=callback, auto_ack=True)

print('consumiendo')


channel.start_consuming()
