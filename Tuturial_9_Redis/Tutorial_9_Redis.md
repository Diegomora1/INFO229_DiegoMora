##   Tutorial Redis con Python

## 1.- Introducción a Redis
Es un sistema de base de datos en memoria de código abierto basado en el almacenamiento de tablas hash. Está escrito en ANSI C por Salvatore Sanfilippo. A diferencia de otros sistemas de almacenamiento de datos que usan el disco, Redis utiliza la memoria principal (RAM) por lo que sus tiempos de acceso son inferiores al milisegundo. Está diseñado para usarse como una base de datos volátil como caché pero eventualmente puede implementarse de forma persistente. Entre sus principales aplicaciones están los videojuegos, sistemas en tiempo real, chat/mensajería, etc.

El objetivo de este tutorial es lograr integrar entender qué es y cómo funciona Redis para luego realizar la integración con Python en un programa simple. 

## 2.- Instalación para sistemas Linux
#### 2.1.- Instalar Python 3

    sudo apt install python3-pip
    
#### 2.2.- Instalar el paquete de Redis para Python usando pip

    pip3 install redis
    
#### 2.3.- Instalar el servidor de redis

    sudo apt-get install redis-server

## 3.- Ejemplo "Hola mundo" con Redis


 Primero se importa la librería de Redis a nuestro programa.

    import redis

Luego, se definen los parámetros de conexión para Redis.

    redis_host = "localhost"
    redis_port = 6379
    redis_password = ""

A continuación se define el objeto de conexión con Redis usando los parámetros definidos.

    r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    
Una vez hecho esto se puede almacenar mensajes usando la instancia de conexión de Redis.

    r.set("msg:hello", "Hola Mundo!")
De la misma forma se puede recuperar un mensaje de memoria según su clave.

    msg = r.get("msg:hello")

Siguiendo este esquema se puede comenzar a trabajar con Redis y entender su funcionamiento y eventualmente incorporar a un proyecto mas grande aprovechando todas las ventajas que este tecnología ofrece.

##### Fuentes: 
##### https://opensource.com/article/18/4/how-build-hello-redis-with-python 
##### https://redis.io/


