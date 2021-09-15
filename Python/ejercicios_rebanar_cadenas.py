"""
numeros: list =[]
for n in range(1,101):
    numeros.append(n)
lista1=numeros[:50]
lista2=numeros [50:]
list1=0
for n in lista1:
    lista1[list1]=n*n
    list1+=1


print (lista1)
list2=0
for n in lista2:
    lista2[list2]=n*n
    list2+=1


print (lista2)
"""
lista_nombres=[]
def nombres_estudiantes (lista:list,nombres:str):
    lista.append(nombres)
    return lista

def pregunta():
    opc="-1"
    estudiantes=[]
    while opc != "0":
        opc2="s"
        opc=input('¿Desea agregar  estudiantes? "1" para sí o "0" para no: ')
        if opc=="1":
            while opc2 == "s":
                preguntar_nombres= input ("Escribe el nombre quieras agregar: ")
                estudiantes= nombres_estudiantes(estudiantes, preguntar_nombres) 
                opc2=input('¿Desea seguir agregando nombres? "s" para si o "n" para no: ')
                if opc2=="n":
                    opc3="0"
                    opc3=input("¿Quiere ver todos los estudiantes? 's' para si 'n' para no: ")
                    if opc3=="s":
                        print(estudiantes)
                    

pregunta()