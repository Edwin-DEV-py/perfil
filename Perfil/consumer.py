import os
import django
#obtener las configuraciones del settings para poder ejecutar este archivo
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Cart.settings')
django.setup()

import pika, json
from AppPerfil.models import Profile

#conectar con cloudAMQP
params = pika.URLParameters('amqps://rlvgzuul:IR8L9U8f_vzjLAF0P4gtt9ALoMC4Q8W7@jaragua.lmq.cloudamqp.com/rlvgzuul')
connection = pika.BlockingConnection(params)
channel = connection.channel()
print('conectado')
#definir el canal
channel.queue_declare(queue='perfil',durable=True)#anadir durable=True para que los mensaje lleguen a pesar de que este apagado
#implementa el protocolo de mensajeria AMQP para declarar una cola.
#una cola es un destino donde los productores envian mensajes y los consumidores reciben. este protocolo crea una cola.

#funcion para saber que obtuvo los datos
def callback(ch, method,properties, body):
    print('resibido en perfil')
    
    data = json.loads(body)
    
    if properties.content_type == 'crear_perfil':
        username = data['user']
        Profile.objects.create(user=username)
        print(f'Perfil creado para el usuario: {username}')
        
        
channel.basic_consume(queue='perfil', on_message_callback=callback, auto_ack=True)

print('consumiendo')


channel.start_consuming()

channel.close()