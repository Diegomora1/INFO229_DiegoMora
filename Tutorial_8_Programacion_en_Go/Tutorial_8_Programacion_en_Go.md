# Tutorial Programación en Go en sistemas Linux
## 1. Introducción a Go
Go o también conocido como GoLang es un lenguaje de programación de código abierto desarrollado en Google por Robert Griesemer, Rob Pike y Ken Thompson. Go es compilado e inspirado en la sintaxis de C. Se encuentra disponible para sistemas Windows, GNU/Linux, Mac OSX, entre otros en formato binario. Es un lenguaje compilado, concurrente, imperativo, estructurado y orientado a objetos. Go ha madurado con el tiempo volviéndose muy popular siendo parte del desarrollo de tecnologías actuales Docker, Kubernetes, Terraform y Ethereum.
## 2. Instalación en sistemas GNU/Linux
2.1. Descargar el archivo comprimido desde la página oficial https://golang.org/doc/install correspondiente a sistemas Linux, luego extraerlo en /usr/local, creando un árbol Go en /usr/local/go de la siguiente forma:

    tar -C /usr/local -xzf go1.15.6.linux-amd64.tar.gz

2.2. Añadir usr/local/go/bin a la variable de entorno PATH

    export PATH=$PATH:/usr/local/go/bin
2.3 Finalmente verificar que la instalación se haya realizado correctamente escribiendo en la terminal lo siguiente:

    go version

## 3. Estructura de un programa en Go
Básicamente todo programa en Go consta de las siguientes partes:

 - Declaración de paquetes o **packages**
 - Importar los paquetes
 - Funciones
 - Variables
 - Instrucciones y expresiones
 - Comentarios

## 3. Tipos de datos en Go 
Al igual que en muchos lenguajes de programación, Go admite una gran variedad de tipos de datos, los cuales pueden clasificarse en:
|Tipo| Descripción |
|--|--|
|Booleano  |Tipo de dato booleano que solo puede encontrarse en dos valores, true o false  |
|Numérico  |Tipo de dato para representar números, ya sea enteros o punto flotante |
|String  | Tipo de dato para almacenar cadenas de texto |
|Derivados|Aquí se incluyen tipo puntero, arreglos, tipo struct, tipo function, tipo slice, tipo interace, tipo map y tipo channel|
   
 ## Variables
 Al declarar una variable se le dice al compilador cuanta memoria es necesaria para almacenar. La sintaxis básica para declarar una variable en Go es:
 

    var <identificador> tipo_dato_opcional

 Por ejemplo:
 

    var j int 
    var c string
    var num float32
  También se pueden inicializar variables directamente sin especificar el tipo de dato, en este el compilador se encarga de identificar el tipo de dato según su valor.
  

    d = 5 // Variable de tipo int 

 
## 4. Estructuras de control
Cuando se requiere de toma de decisiones y ciclos iterativos en nuestro programa debemos hacer uso de las estructuras que Go ofrece para ello. En general, dichas estructuras tienen una estructura similar a las del lenguaje C.

Estructura condicional **if** 

    if(condicion){
	    // Intrucciones que se ejecutan si la condicion es verdadera
	}else{
		// // Intrucciones que se ejecutan si la condicion es falsa
Si se requiere se pueden incluir varios if siguiendo la misma estructura con diferentes condiciones, lo que se conoce como if anidados.

En el caso de los ciclos, Go tiene la instrucción **for** que realiza la función de dos estructuras comunes en otros lenguajes de programación como lo son for y while. Por tanto, la sintaxis de un for en Go puede tomar principalmente dos formas:

   
    * Tipo while
    for(condicion){
	    // Intrucciones que se ejecutan mientras la condición sea verdadera.
	}    
	* Tipo for
	for(inicio; condicion; incremento){
		// Intrucciones	
	}

## 5. Funciones
Una función es un grupo de instrucciones que en conjunto realizan una determinada tarea. Aparte de todas las funciones que puede definir el usuario, todo programa en Go tiene una función main(). La declaración de una nueva función le dice al compilador el nombre, tipo de retorno y los parámetros de esta. La estructura para declarar una función es:

    func nombre_funcion([lista_parametros]) [tipo_retorno] 
    {
	    // Cuerpo de la función
	}    

## 6. Hola Mundo en Go
Primero creamos el archivo hola.go en nuestro directorio de trabajo, luego completamos con lo siguiente:


    package main
    
    import "fmt"
	
	func main(){
		fmt.Println("Hola Mundo!")
	}

Opcionalmente se puede compilar el programa y luego ejecutar, sin embargo, con el comando go run podemos ejecutar directamente nuestro programa en un solo paso. Escribimos en la consola:

    go run hola.go

    
 Salida:
 

    Hola Mundo!



### Fuentes
 - https://golang.org/
 - https://www.linuxparty.es/54-programacion/10105-tutorial-de-introduccion-a-la-programacion-con-go
 - https://www.tutorialspoint.com/go/index.htm
