# SistemasDistribuidos

##Práctica 3 - Twitter
####Práctica realizada por Antonio Gambín y Francisco Pastor
- - -
###Enunciado
Vamos a desarrollar un programa en Python, que revise las direcciones (latitud y longitud) de los tweets que   cumplan una determinada opción, como que sea el más actual, que corresponda a alguna afición (equipo de fútbol,   políticas..) y desplegar esas direcciones en un mapa utilizando la extensión de ​ Flask ​ para Google Maps. 
---
####¿Qué haremos para desarrollar dicho ejercicio?
Lo haremos desarrollando el ejercicio de la siguiente manera:

####![center](https://cdn2.iconfinder.com/data/icons/oxygen/48x48/actions/note2.png) Primera parte del algoritmo:
Empleando la función definida en el módulo twitterAPI.py, nos conectamos a nuestra cuenta de twitter con la información introducida en la función "oath_login()

####![center](https://cdn2.iconfinder.com/data/icons/oxygen/48x48/actions/note2.png) Segunda parte del algoritmo:
Imprimimos información al usuario y realizamos la búsqueda del tema a buscar(Tweets sobre el Betis C.F) y buscamos en el contenedor en el que hemos almacenado el resultado de la búsqueda, la localización de dichos tweets para su representación gráfica en el mapa.
####![center](https://cdn2.iconfinder.com/data/icons/oxygen/48x48/actions/note2.png) Tercera y última parte del algoritmo:
Una vez tenemos los datos de posicionamiento de los tweets, lanzamos nuestra aplicación encargada de representar nuestro mapa, localizando las coordenadas obtenidas en el apartado anterior.
---
Fin del Readme
---

