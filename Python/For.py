


numeros =range(0,1)

for n in numeros:
    print(n)

print("Fin del for")
print("_______________________________")
nombres= ["Pedro", "Juan","Martha",2,True,3.5]

#Acceder a una posición en específico
nombres[1]= "Angel" #Cambiar el valor en la lista
print(nombres[1])
"""
index= 0
for nom in nombres:
   # if index%2==0:    #para que vaya en dos en dos
    print(nom)
   # index +=1     #para que vaya en dos en dos
"""
"""
def actualizacion_de_notas(notas_est):
    x=0
    for n in notas_est:
        nueva_nota = float(input("Por favor ingrese una nota: "))
        notas_est[x] = nueva_nota
        x+=1
    return notas_est

lista_notas = [3.2, 5, 4]
actualizacion_de_notas(lista_notas)

"""

"""
numeros= range(0,101,2)
index =0

for n in numeros:
    print(numeros[index])
    index+=1

numeros= range(100,0,-2)
index =0

for n in numeros:
    print(numeros[index])
    index+=1
"""
"""

apellidos = [ "Perez", "Quintero","Morales"]

for cadena in apellidos:
    print(cadena)

"""
"""
Num1 = int(input("Ingrese el número inicial del conteo: "))
Num2= int(input("Ingrese el número final del conteo: "))
Conteo= range(Num1,Num2,3)

for n in Conteo:
    print (n)


"""

num1= int(input("Ingrese un número positivo: "))
num2= num1+num1

conteo= range(num1,num2)
for n in conteo:
    print(n)

