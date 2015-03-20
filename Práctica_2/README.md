# SistemasDistribuidos

##Práctica 2 - Pokemon
####Práctica realizada por Antonio Gambín y Francisco Pastor
- - -
###Enunciado
Vamos a desarrollar el programa de Python que nos permita, a partir de una lista de palabras, encontrar la lista más larga posible de palabras de manera que la última letra de una palabra coincida con la primera de la siguiente palabra. Para probar el programa, la lista de palabras con las que vamos a trabajar son la que encontramos en el fichero ​pokemon.txt

---
####¿Qué haremos para desarrollar dicho ejercicio?
Lo haremos desarrollando el ejercicio de la siguiente manera:

####![center](http://gpxplus.net/files/images/achievements/ProfessorOak.png) Primera arte del algoritmo:
- Tendremos que reconocer el archivo txt, en nuestro caso *(pokemon.txt)*, para recolectar todos los elementos de los pokemons citados.
- Almacenaremos todos los elementos en una lista, a fin de una mejor disponibilidad por parte del programador.

####![center](http://gpxplus.net/files/images/achievements/ProfessorOak.png) Segunda parte del algoritmo:
- Desarrollaremos las funciones auxiliares, que nos servirán de ayuda a la hora de hayar la mayor combinación:
	- Función **buscar**: esta función nos devolverá un booleano para comprobar que la palabra que deseamos buscar, se encuentra dentro de la lista pedida.
  
			def buscar(lista, palabra):
			    return palabra in lista

	- Función **mayor o igual a que**: esta función nos devolverá la lista de mayor tamaño.

			def operator_mayor (lista1, lista2):
			    if len(lista1)>len(lista2):
			        return lista1
			    else:
			        return lista2

	- Función **Primer Carácter**: esta función nos devolverá el primer carácter de una palabra que le solicitemos.

			def primerCaracter(palabra):
			    return palabra[0]

####![center](http://gpxplus.net/files/images/achievements/ProfessorOak.png) Tercera y última parte del algoritmo:
Para comprender mejor la última parte del algoritmo, incluiré primero el código y luego lo iré explicando línea a línea.

	for i in range(len(pokedex)):
        pokedex_temporal.append(pokedex[i])
        l=0
        while l<len(pokedex):
            if buscar(pokedex_temporal, pokedex[l])==False:
                if pokedex_temporal[len(pokedex_temporal)-1].endswith(primerCaracter(pokedex[l]))==True:
                    pokedex_temporal.append(pokedex[l])
                    l=0
                else:
                    l=l+1
            else:
                l=l+1

        pokedex_nacional= operator_mayor(pokedex_nacional, pokedex_temporal)
        pokedex_temporal=[]
	
- Primero desarrollaremos una búsqueda de pokemon en pokemon, paso por paso,para elegir la mejor combinación. Iré explicando lo que sucede en cada iteración:
	- En el primer ciclo del bucle, incluiremos el primer pokemon en una lista temporal, para así partir de una base. A continuación, recorremos la lista original, siguiendo una serie de condiciones:
		- Mientras que un pokemon no esté en la lista temporal,
		- Mientras que un pokemon concuerde su primer carácter con el último carácter del último pokemon que se encuentre en la lista temporal,
		- Incluiremos dicho pokemon, en la lista temporal, y volveremos a recorrer dicha lista original, por si en la nueva iteración, concuerda algunos de la totalidad de la lista.
	- En la segunda vuelta escogeremos como pokemon inicial el segundo pokemon de la lista y compararemos el resultado obtenido con la anterior teniendo siempre en una variable final la combinación más larga.
- Una vez realizado dicho bucle, obtendremos dicha combinación.

---
Fin del Readme
---
![center](http://37.media.tumblr.com/4d5af1975806d9eeab9735145c483254/tumblr_n7rhblz9cL1qlwf8co9_400.gif)

