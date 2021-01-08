#!/usr/bin/env python3

#Se importa el paquete de redis
import redis

# Se definen los parametros de conexion con redis
redis_host = "localhost"
redis_port = 6379
redis_password = ""


def hello_redis():
    
    try:
        # Se crea el objeto de conexion con redis
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
   
        # Se guarda el mensaje en redis
        r.set("msg:hello", "Hello Redis!!!")

        # Se recupera el mensaje de Redis
        msg = r.get("msg:hello")
        print(msg)        
   
    except Exception as e:
        print(e)


if __name__ == '__main__':
    hello_redis()

