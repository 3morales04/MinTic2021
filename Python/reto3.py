import os
os.system('clear')


"""
=================================================================
======================VARIABLES GLOBALES=========================
=================================================================
"""

# VARIABLE QUE ALMACENA LA CONTRASEÑA DEL PROGRAMA
global password
password = '03615'

# Lista de opciones
global listamenu
listamenu = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana", "Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo", "Elegir opción de menú favorita", "Cerrar sesión"]

# "Matriz" (lista compuesta) para almacenar las coordenadas
#global coordenadas
# Se le indica que será una lista de listas con valores flotantes
"""
[
    [lat_1, lng_1],
    [lat_2, lng_2],
    [lat_3, lng_3]
]
"""
coordenadas: list = []

"""
=================================================================
====================FUNCIONES DEL PROGRAMA=======================
=================================================================
"""

"""
Grafica el menú en consola así:

1. Cambiar contraseña
2. Ingresar coordenadas actuales
3. Ubicar zona wifi más cercana
4. Guardar archivo con ubicación cercana
5. Actualizar registros de zonas wifi desde archivo
6. Elegir opción de menú favorita
7. Cerrar sesión
Elija una opción: 
"""


def menu():
    #os.system('clear')
    print("")
    cont: int = 1
    for x in listamenu:
        print(f"{cont}. {x}")
        cont += 1
    opmenu = None
    try:
        opmenu = int(input("Elija una opción: "))
    except:
        opmenu = 0
    return (opmenu, listamenu[opmenu-1])


"""
=============FUNCIONES DEL RETO 2 ==================
"""


def opcion_6():  # se hace el intercambio de las opciones del menu.
    opfavorita = int(input("Seleccione opción favorita: "))
    if (opfavorita >= 1 and opfavorita <= 5):
        adv = int(input("¿Cuánto son tres medias moscas y mosca y media? "))
        if (adv == 3):
            adv2 = int(input(
                "Para confirmar por favor responda: De millones de hijos que somos el primero nací, pero aun así soy el menor de todos. ¿Quién soy? : "))
            if (adv2 == 0):
                os.system('clear')
                aux = listamenu[0]
                listamenu[0] = listamenu[(opfavorita-1)]
                listamenu[(opfavorita-1)] = aux
            else:
                print("Error")
                funcion_reto2()
        else:
            print("Error")
            funcion_reto2()
    else:
        print("Error")
        exit()


def funcion_reto2():
    # Sub programa
    contint = 0  # cuenta el numero de intens fallido y se sale del menu al ser igual a 3
    opmenu = 1  # se inicializa en 1 para que entre por primera vez al while
    # ciclo repetitivo para controlar el menu
    while (opmenu != 7 and contint != 3):
        #os.system('clear')
        opmenu = menu()
        # controlo que las opciones del menu esten entre 1 y 7
        if (opmenu[0] > 7) or (opmenu[0] <= 0):
            contint += 1
            print("Error")

        elif opmenu[0] == 6:
            opcion_6()
            os.system('clear')
        elif (opmenu[0] == 7):
            print("Hasta pronto")
            exit()
        else:
            print(f"Usted ha elegido la opción {opmenu[0]}")
            if opmenu[1] == "Cambiar contraseña":
                cambiar_password()
            elif opmenu[1] == "Ingresar coordenadas actuales":
                actualizar_coordenadas()
            else:
                exit()
        os.system('clear')


"""
=============FUNCIONES DEL RETO 3 ==================
"""

# Funcion para cambiar la contraseña del usuario


def cambiar_password():
    os.system('clear')
    global password
    # Solicita la contraseña actual al usuario para validar
    pass_actual: str = input("Ingrese contraseña actual: ")
    # Valida que la contraseña ingresada corresponda con la actual
    if pass_actual == password:
        # Solicita la nueva contraseña
        nueva_pass: str = input("Nueva contraseña: ")
        # Valida que la contraseña nueva no sea igual a la actual
        if nueva_pass == password:
            os.system('clear')
            print("Error")
            exit()
        else:
            password = nueva_pass
            funcion_reto2()
    else:
        os.system('clear')
        print("Error")
        exit()

# Función para permitir al usuario ingresar las 3 coordenatas por primera vez (lat, lng)


def crear_coordenadas():
    os.system('clear')
    # Contador
    cont: int = 0
    while cont < 3:
        # Referencia la variable global
        global coordenadas
        # Solicita al usuario la latitud
        lat: float = float(input(f"Por favor ingrese latitud {cont+1}: "))
        if lat >= 5.888 and lat <= 6.306:
            # Solicita al usuario la longitud
            lng: float = float(input(f"Por favor ingrese longitud {cont+1}: "))
            if lng >= -72.552 and lng <= -72.321:
                sitio: list = [lat, lng]
                coordenadas.append(sitio)
                cont += 1
            else:
                os.system('clear')
                print("Error coordenada")
                exit()
        else:
            os.system('clear')
            print("Error coordenada")
            exit()

# Funcion para actualizar coordenadas


def actualizar_coordenadas():
    os.system('clear')
    # valida si existen coordenadas en la lista
    if len(coordenadas) == 0:
        crear_coordenadas()
    else:
        cont: int = 1
        for c in coordenadas:
            print(
                f"Coordenada [latitud, longitud] {cont} : ['{c[0]}', '{c[1]}']")
            cont += 1
        print("La coordenada 1 es la que está mas al norte")
        print("La coordenada 2 es la que está mas al sur")
        # Se solicita la opción al usuario
        opc: int = int(input(
            "“Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú "))
        if opc >= 1 and opc <= 3:
            # Solicita al usuario la latitud
            lat: float = float(input(f"Por favor ingrese latitud {opc} : "))
            if lat >= 5.888 and lat <= 6.306:
                # Solicita al usuario la longitud
                lng: float = float(input(f"Por favor ingrese longitud: {opc}: "))
                if lng >= -72.552 and lng <= -72.321:
                    sitio: list = [lat, lng]
                    coordenadas[opc-1] = sitio
                else:
                    os.system('clear')
                    print("Error actualización")
                    exit()
            else:
                os.system('clear')
                print("Error actualización")
                exit()
        elif opc == 0:
            funcion_reto2()
        else:
            print("Error actualización")
            exit()

# Funcion para validar coordenadas, retorna true si los datos son válidos, false de lo contrario

"""
def validar_coordenadas(lat: float, lng: float) -> bool:
    # Bandera que me infica si el rango de las coordenadas son validas o no
    rango_valido: bool = False
    # Valida el rango de las coordenadas
    if (lat >= 5.888 and lat <= 6.306) and (lng >= -72.552 and lng <= -72.321):
        # Actualiza la bandera a True
        rango_valido = True
    # Retorna la bandera
    return rango_valido
"""

"""
=============FUNCION PRINCIPAL DEL PROGRAMA ==================
"""
# Programa Principal


def main():
    """
    -------------------Bloque de código del reto 1 ---------------------------
    """
    print('Bienvenido al sistema de ubicación para zonas públicas WIFI')
    try:
        usuario = 51630
        usuario_in = int(input("Nombre de usuario: "))
        if usuario != usuario_in:
            print("Error")
            exit()
        else:
            password_in = input("Digite la Contraseña: ")
            if password == password_in:
                captcha1 = 630
                captcha2 = (5+1)-(6*1)+1+1+1
                captchat = captcha1 + captcha2
                print("La suma de: ", captcha1, "+", captcha2)
                captcha_in = int(input())
                if captcha_in == captchat:
                    os.system('clear')
                    print("Sesión iniciada")
                    """
                    ----------------------Redirige a las funcionalidades del Reto 2---------------------
                    """
                    # Llama a la función del reto 2
                    funcion_reto2()
                else:
                    print("Error")
                    exit()
            else:
                print("Error")
                exit()
    except ValueError:
        os.system('clear')
        print("Error")


# Llamar a la función principal de mi programa
main()
#funcion_reto2()
