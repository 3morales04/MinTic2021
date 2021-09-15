"""
import numpy as np

matriz = np.array([1,2,3,4]) 
numeros: list = [1,2,3,4]

print(numeros)
print(matriz)
lista_compuesta: list= [[1,2],[3,4]]
matriz_compuesta: list= np.array([[1,2],[3,4]])
print(lista_compuesta)
print(matriz_compuesta)
#-----------------------------------------------

lista_1: list = [1,2,3,4]
lista_2: list = [5,6,7,8]
resultado_listas = lista_1+lista_2
print(resultado_listas)

matriz_1 = np.array([[1,2,3,4]])
matriz_2 = np.array([[5,6,7,8]])
resultado_matriz = matriz_1+matriz_2

print(resultado_matriz)

m1= np.array([ [5,2], [10,8] ])
m2 = np.array([[1,4],[6,8]])
suma_matriz = m1+m2
print(suma_matriz)
"""
#-----------------------------------------
#Creacion de una lista compuesta 2x2
"""
    a b
    b d
"""
#numpy
lista_compuesta: list = [ ["a","b"], ["c", "d"] ]
#Fila cero
print( lista_compuesta[0] )
#Obtenemos el valor de la columna cero
print( lista_compuesta[0][0]+" "+lista_compuesta[1][1] )
print( lista_compuesta[1][1] )
#
print( "".join(lista_compuesta[0]) )


"""
---------------COMPARATIVA ENTRE NUMPY Y LISTAS COMPUESTAS---------------------
"""
print("---------------COMPARATIVA ENTRE NUMPY Y LISTAS COMPUESTAS---------------------")
#Importamos numpy
import numpy as np
#Importamos libreria del sistema
import sys
#Creamos un rango de numeros
rango = range(1000)
#Imprimir el espacio en memoria que ocupa una lista de mil elementos
print( sys.getsizeof(1)*len(rango) )

#Creamos una matriz de una fila con mil columnas
matriz = np.arange(1000)
print( matriz.size*matriz.itemsize )

print("-----------------CALCULANDO EL TIEMPO DE EJECICION--------")
import time #Librería que nos permite trabajar con el tiempo del sistema
tamanio: int = 10000000
l1 = range(tamanio)
l2 = range(tamanio)
result: list = []
index = 0
tiempo_inicial = time.time()#Obtener el tiempo en milisegundos
for n in l1:
    suma = n + l2[ index ]
    result.append(suma)
    index += 1

print(time.time() - tiempo_inicial)

m1 = np.arange(tamanio)
m2 = np.arange(tamanio)
tiempo_inicial = time.time()
suma = m1+m2
print(time.time()-tiempo_inicial)



