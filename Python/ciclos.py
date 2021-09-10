"""
Desarrolle un programa que solicite los nombres de N 
estudiantes y los almacene en una lista.
Posteriormente permitir buscar al usuario un estudiante (indicarle 
si el estudiante existe o no existe en la lista)
"""

lista: list = ["juan", "pedro"]

#Función para insertar un estudiante en una lista
def insertar_estudiante(lista: list, nombre_estudiante: str)->list:
    #inserta al final de la lista un nuevo elemento
    lista.append(nombre_estudiante)
    #Retorna la lista con el nuevo elemento insertado
    return lista

def buscar_estudiante(lista: list, nombre_estudiante: str)->bool:
    resp: bool = False
    #Iteramos la lista de estudiantes
    for n in lista:
        #Compara el estudiante a buscar con cada elemento de la lista
        if n == nombre_estudiante:
            resp = True
    #Retornamos un booleano (True si encuentra al estudiante - False en caso contrario)
    return resp

def menu():
    #Creamos una lista vacia de estudiantes
    estudiantes: list = []
    opc_menu: int = -1
    while opc_menu != 0:
        opc = 'S'
        print("---------------------------------------------")
        print("1 --> Añadir nuevos estudiantes")
        print("2 --> Buscar un estudiante")
        print("3 --> Mostrar todos los estudiantes")
        print("0 --> Salir")
        print("---------------------------------------------")
        opc_menu = int( input("Por favor ingrese una opción: ") )

        if opc_menu == 1:
            """
            con .upper() convertimos una cadena a mayúscula
            Ejemplo: s.upper() -> S - hola.upper() -> HOLA
            """
            while opc.upper() == 'S':
                #Solicitamos el nombre del estudiante
                nombre_estudiante = input("Por favor ingrese el nombre del estudiante: ")
                #Inserto el nuevo elemento en la lista y sobreescribo la lista original
                estudiantes = insertar_estudiante(estudiantes, nombre_estudiante)
                #Preguntamos al usuario si quiere continuar ingresando nombres
                opc = input("¿Desea continuar ingresando nombres de estudiantes? S (si) - N(no): ")
        elif opc_menu == 2:
            #Solicitamos el nombre del estudiante a buscar
            nombre_estudiante = input("Nombre del estudiante que desea buscar: ")
            #Obtenemos un valor booleano de la búsqueda del estudiante
            resp = buscar_estudiante(estudiantes, nombre_estudiante)
            #Validamos si la búsqueda fue satisfactoria
            if resp:
                print("El estudiante existe en la lista")
            else:
                print("El estudiante no existe en la lista")
        elif opc_menu == 3:
            print(estudiantes)

#Llamamos la función principal (menu())
menu()

