"""
Solicitar al usuario las N ventas generadas,
posteriormente imprimir el promedio
"""

"""-------WHILE-------"""
"""
#Variable que almacena la sumatoria de las ventas
ventas: float = 0
#Variable que almacena la opción ingresada por el usuario (-1 parar el ciclo)
opc = 0
#Variable que me representa un contador para calcular el promedio
cont = 0
while opc != -1:
    ventas += float( input("Por favor ingrese las ventas generadas: ") )
    cont += 1
    opc = int( input("¿Desea continuar? -1 (No) 0(si)") )

#Calculamos el promedio
promedio = ventas/cont
#Imprimimos el promedio
print("Promedio de ventas: ", promedio)
"""

"""--------FOR--------"""
"""
#Solicitamos el número de itaraciones a realizar en el for
num_ventas = int( input("Ingrese el número de ventas a digitar: ") )
#Creamos una lista de tamaño 'num_ventas'
rango_iteracion = range(num_ventas)
ventas = 0
#Creamos el for
for _ in rango_iteracion:
    ventas += float( input("Por favor ingrese las ventas generadas: ") )
#Calcular el promedio
if num_ventas == 0:
    print("No hay promedio para mostrar")
else:
    promedio = ventas/num_ventas
    print("El promedio de ventas es: "+str(promedio))
"""
"""
De un listado de alumnos, imprimir los
que se enuentran en una posición impar, con el siguiente formato:
nombre1 - nombre2 - ...
"""
"""
#Listado de los nombres de estudiantes
alumnos = ["juan", "pedro", "andres", "martha", "luisa"]
#Variable que representa el índice de la lista durante la interación
index = 0
nombres_concatenados = ""
#Iteramos la lista de alumnos
for nombre in alumnos:
    if index%2 != 0:
        nombres_concatenados += nombre +" - "
    index += 1

print(nombres_concatenados)
"""
lista=[2,3,4,5,7,6]
for x in lista:
    if x%2==0 :
        print(x)







