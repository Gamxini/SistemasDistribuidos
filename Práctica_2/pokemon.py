#Declaración de funciones
def leertxt(nombre):
    f=file(nombre, "r")
    list_poke =f.read().split()
    return list_poke

def list_comb(pokedex):
    pokedex_temporal=[]
    pokedex_nacional=[]
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

    return pokedex_nacional

def buscar(lista, palabra):
    return palabra in lista

def operator_mayor (lista1, lista2):
    if len(lista1)>len(lista2):
        return lista1
    else:
        return lista2

def primerCaracter(palabra):
    return palabra[0]
    
#Comienzo del Programa principal
list_poke = leertxt("pokemon.txt")
pokedex_nacional = list_comb(list_poke)
print "El tamano total de tu pokedex es de "
print len(pokedex_nacional)
print "Enhorabuena! Echemos un vistazo a esos pokemons:"
print (pokedex_nacional)
