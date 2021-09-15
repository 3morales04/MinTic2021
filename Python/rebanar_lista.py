
#Lista de números
numeros: list = ["1","2","3","4","5","6", "3"]
#Acceder a una posición en específico
print( int(numeros[1]) )
#Rebanar una lista [desde : hasta]
print( numeros[0:3] )
print( numeros[:3] )
#Desde la posición 3 hasta el final de la lista
print( numeros[3:] )

print(numeros[0:5:2])

#Elimina el ultimo elemento
numeros.pop()
#Elimina un elemento en una posición en especifico
numeros.pop(0)
#Eliminar un elemento con el nombre/valor del elemento
numeros.remove("3")

print("----------------------------------")
letras1: list = ['a', 'b', 'c', 'd']
letras2: list = ['e', 'f', 'g']
#Concatenamos/unimos dos listas
letras: list = letras1 + letras2
print(letras)
#Concatenar una lista a un string
print( "".join(letras) )
#Limpiar una lista
#letras.clear()
#print(letras)
referencia_letras = letras
print(referencia_letras)
print("------Referencia de lista-------------")
#Modificar la lista original
letras[0] = 'z'
print(referencia_letras)
referencia_letras[4] = 'J'
print("Letras: ")
print(letras)
print("-----------Copia de lista------------")
#Crear una copia de mi lista
copia_lista = letras.copy()
#Modificamos un valor de la lista original
letras[1] = 'x'
print(copia_lista)
copia_lista[3] = 'h'
print(letras)
print("-----Ordenar una lista------")
lista_numerica: list = [6,5,9,10,1,5,2,8,3]
#Ordenar una lista descendente
lista_numerica.sort(reverse=True)
print( lista_numerica )
#Ordenar una lista ascendente
lista_numerica.sort()
print( lista_numerica )

frutas: list = ['banana', 'anon', 'tamarindo']
frutas.sort()
print(frutas)

tamanio = len(frutas)
print("El tamaño de la lista frutas es: ", tamanio)
print("Ultimo elemento de frutas: ", end="")
print( frutas[tamanio-1] )

"""
------------CADENA DE CARACTERES--------------
"""
"""
#Rebanando cadenas de caracteres
cadena: str = "Hola"
print( cadena[0:2] )
#Acceder a un caracter en específico
print(cadena[2])
"""
