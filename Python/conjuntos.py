conjunto_numeros1: set = {1,2,3,4,5,6}
conjunto_numero2 = {1,5,8,9,10}
#crear conjunto vacío
conjunto_vacio = set()
#Elementos en común
interseccion= conjunto_numeros1.intersection(conjunto_numero2)

print(interseccion)

#Retorna los valores que están en el conjunto1 pero no en el 2 no cambian los conjuntos
res=conjunto_numeros1-conjunto_numero2
print(res)

#imprime y actualiza los valores que están en el conjunto1 pero no en el 2
conjunto_numeros1.difference_update(conjunto_numero2)
print(conjunto_numeros1)
