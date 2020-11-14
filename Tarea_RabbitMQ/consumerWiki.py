#!/usr/bin/env python
import pika, sys, os, wikipedia

def main():

    #Conexión al servidor RabbitMQ   
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    #Nos aseguramos que existe una cola 'hello'
    channel.queue_declare(queue='wikipediaMQ')


    #Recibir mensajes de la cola es más complejo. Funciona suscribiendo una función de devolución de llamada ("callback"). Cada vez que recibimos un mensaje, esta función "callback" es llamada por la libreria Pika. En nuestro caso, esta función imprimirá en la pantalla el contenido del mensaje.
    def callback(ch, method, properties, body):
        search = wikipedia.search(body)
        print("[X] Received")
        print("Los resultados de busqueda para "+str(body)+" en Wikipedia son:")
        print(search)

    channel.basic_consume(queue='wikipediaMQ', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    #Bucle infinito
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

