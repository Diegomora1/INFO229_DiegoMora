# Tutorial Ruby on Rails para sistemas GNU/Linux
## 1. ¿Qué es Ruby on Rails?
También conocido con RoR, es un framework para el desarrollo de aplicaciones web de código abierto escrito en el lenguaje de programación Ruby  siguiendo el patrón de arquitectura Modelo Vista Controlador (MVC). Se diseñó con el objetivo de hacer la programación de aplicaciones web mucho más sencilla tratando de incluir todo lo que el programador necesita para comenzar. De esta forma, se requiere escribir mucho menos código para lograr un objetivo en comparación con otros frameworks. Rails se distribuye a través de RubyGems, que es el formato oficial de los paquetes y el canal de distribuición de librerías y aplicaciones Ruby.
Este tutorial tiene como objetivo el desarrollo de una aplicación web Rails básica donde se entregarán las herramientas necesarias para ello.
## 2. Instalación en sistemas GNU/Linux
Para realizar nuestro proyecto es necesario 
2.1. Requisitos previos:

 - Ruby (v2.5.0 o superior)
 - SQLite3
 - Node.js (v8.17.0 o superior)
 - Yarn

2.2 Instalación de Rails
Una vez instalados los requisitos y verificada las versiones se puede proceder a instalar Rails. Para ello utilizamos el siguiente comando provisto por RubyGems:

    gems install rails
Para verificar que la instalación se realizó correctamente, se puede verificar la versión:

    rails --version
## 3. Creando nuestra aplicación web
Rails incluye una gran cantidad de scrips llamados generadores que fueron diseñados para simplificar el desarrollo y permiten la automatización de ciertas tareas. Uno de estos es el generador de aplicaciones que permite crear la base de una aplicación web de manera automática.
Para ejecutar este generador, creamos nuestro directorio de trabajo, navegamos con la terminal hasta nuestro directorio y ejecutamos:

    rails new blog
    
Si todo funciona correctamente, esto generará un subdirectorio blog/ con un conjunto de archivos y directorios dentro que forman la estructura de una aplicación Rails. A continuación, se da una breve descripción a cada uno de estos componentes.
|Archivo/Directorio|Descripción  |
|--|--|
|app/  | Contiene los controladores, modelos, vistas, canales y assets de nuestra aplicación. |
|bin/|Contiene el script rails que la aplicación puede contener otros para configurar por ejemplo la actualización o el despliegue de la aplicación.|
|config/|Contiene la configuración de las rutas, bases de datos, entre otros de nuestra aplicación.|    
|config,ru|Configuración Rack para servidores basados en Rack usados para iniciar la aplicación.|
|db/|Contiene el esquema de las bases de datos.|
|Gemfile/Gemfile.lock|Estos archivos permiten especificar las dependencias gem de nuestra aplicación|
|lib/|Contiene los módulos extendidos de la aplicación|
|log/|Contiene los archivos log de nuestra aplicación|
|package.json|Este archivo permite especificar las dependencias npm que son necesarias para la aplicación. Este archivo es usado por Yarn.
|public/|Contiene archivos estáticos y assets compilados de la apliación|
|Rakefile|Este archivo localiza y carga tareas que pueden ser ejecutadas desde la consola|
|README,md|Este archivo se utiliza para describir nuestra aplicación y servir como manual de usuario|
|storage/|Almacenamiento activo de archivos. |
|test/|Contiene pruebas unitarias, fixtures, entre otros archivos alusivos al testeo.|
|tmp/|Archivos temporales.|
|vendor/|Contiene todo el código proveniente de fuentes externas.|
## 4. Hola Mundo en Rails
En este punto, ya tenemos una aplicación Rails funcional, de hecho podemos ejecutarla posicionados en el directorio blog/ y ejecutando en la consola:

    bin/rails server
Este comando pone a correr la aplicación en http://localhost:3000 y podemos ver el mensaje de Rails "Yay! You're on Rails!" junto con una imagen por defecto.

Para realizar nuestro cometido de decir "Hola Mundo", debemos como mínimo crear una ruta, un controlador con una acción y una vista. Una ruta mapea una petición a una acción de controlador. Una vista despliega información en el formato deseado.
Vamos a comenzar añadiendo una nueva ruta a nuestro archivo de rutas config/routes.rb 

    Rails.application.routes.draw do
	    get "/articles", to: "articles#index"
	end    
La ruta creada declara que las consultas get de /articles son mapeadas a la acción index del ArticlesControler.
Para crear el ArticlesControler junto con la acción index usamos el generador de controladores con el siguiente comando:

    bin/rails generate controller Articles index --skip-routes

Con esto Rails creará una serie de archivos. El mas importante es el archivo controlador app/controllers/articles_controler.rb. La acción index está vacía y se corresponde con el archivo app/views/articles/index.html.erb, y es el que modificaremos para desplegar nuestro "Hola Mundo" en pantalla con la siguiente etiqueta html:

    <h1>Hola Mundo!</h1>
Luego de esta modificación ejecutamos nuevamente la aplicación:

    bin/rails server
Cuando la aplicación se encuentre corriendo vamos a la dirección http://localhost:3000/articles y encontraremos nuestro mensaje.

### Fuentes
- https://guides.rubyonrails.org/index.html
- https://es.wikipedia.org/wiki/Ruby_on_Rails
