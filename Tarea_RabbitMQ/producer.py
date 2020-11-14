#!/usr/bin/env python
import sys, pika

#El mesnaje que se enviara se ingresa como parametro al programa
if(len(sys.argv) > 2):
	app = sys.argv[1]
	msg = sys.argv[2]
else:
	print("Error. El programa debe ejecutarse como python producer.py app msg. Donde app puede ser wikipedia o youtube")
	sys.exit(0)
	

#Conexión al servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#Creación de las cola
channel.queue_declare(queue='youtubeMQ')
channel.queue_declare(queue='wikipediaMQ')

#Seleccion de mensaje
if app == "wikipedia":
	print("wikipedia ayaya")
	mq = "wikipediaMQ"
elif app == "youtube":
	print("youtube gachibass")
	mq = "youtubeMQ"
else:
	print("Error de entrada")
	sys.exit(0)	

#Publicación del mensaje
channel.basic_publish(exchange='',
                      routing_key=mq,
                      body=msg)

print(" [x] Sent "+msg)

connection.close()
