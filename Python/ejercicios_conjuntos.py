"""
Ejercicio: 
"""

#CONJUNTOS
set_placas_1: set = {"RJH-545", "ZMN-821", "MLK-981", "IKJ-987"}
set_placas_2: set = {"RJH-545", "MLK-981", "ASD-986", "IYS-981", "986-JHT"}

#Punto 1
#Obtener las placas que se encuentran en los dos conjuntos
interseccion= set_placas_1.intersection(set_placas_2)

print(interseccion)
#Punto 2
#Obtener los elementos de 'set_placas_1' que no están en 'set_placas_2'
res=set_placas_1-set_placas_2

print(res)
#Punto 3
#Crear un conjunto con todos los elementos de los dos conjuntos
res1 = set_placas_1.union(set_placas_2)
print (res1)

