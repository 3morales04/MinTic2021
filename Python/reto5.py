import json
import math
import os
os.system('clear')
# Importación de la biblioteca matemática


"""
=================================================================
=================VARIABLES GLOBALES RETO 1 Y 2===================
=================================================================
"""

# VARIABLE QUE ALMACENA LA CONTRASEÑA DEL PROGRAMA
#global password
password = '03615'

# Lista de opciones
global listamenu
listamenu = [
    "Cambiar contraseña",
    "Ingresar coordenadas actuales",
    "Ubicar zona wifi más cercana",
    "Guardar archivo con ubicación cercana",
    "Actualizar registros de zonas wifi desde archivo",
    "Elegir opción de menú favorita",
    "Cerrar sesión"]

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


"""
=============FUNCIONES DEL RETO 2 ==================
"""


def menu():
    os.system('clear')
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
        opmenu = menu()
        # controlo que las opciones del menu esten entre 1 y 7
        if (opmenu[0] > 7) or (opmenu[0] <= 0):
            contint += 1
            print("Error")

        elif opmenu[0] == 6:
            opcion_6()
            os.system('clear')
        elif (opmenu[0] == 7):
            os.system('clear')
            print("Hasta pronto")
            exit()
        else:
            print(f"Usted ha elegido la opción {opmenu[0]}")
            if opmenu[1].lower() == "Cambiar contraseña".lower():
                cambiar_password()
            elif opmenu[1].lower() == "Ingresar coordenadas actuales".lower():
                actualizar_coordenadas()
            elif opmenu[1].lower() == "Ubicar zona wifi más cercana".lower():
                ubicar_zonas_cercanas()
            elif opmenu[1].lower() == "Guardar archivo con ubicación cercana".lower():
                guardar_archivo()
            elif opmenu[1].lower() == "Actualizar registros de zonas wifi desde archivo".lower():
                actualizar_zonas_wifi()
            else:
                exit()


"""
=============FUNCIONES DEL RETO 3 ==================
"""
"""
=================================================================
===================VARIABLES GLOBALES RETO 3=====================
=================================================================
"""
# "Matriz" (lista compuesta) para almacenar las coordenadas
# global coordenadas
# Se le indica que será una lista de listas con valores flotantes
"""
[
    [lat_1, lng_1],
    [lat_2, lng_2],
    [lat_3, lng_3]
]
"""
coordenadas: list = []


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
                lng: float = float(
                    input(f"Por favor ingrese longitud: {opc}: "))
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
=============FUNCIONES DEL RETO 4 ==================
"""
"""
=================================================================
===================VARIABLES GLOBALES RETO 4=====================
=================================================================
"""
# Variable que me representa el radio de la tierra
R = 6372.795477598
# Velocidad promedio de un bus y moto m/s
velocidad_bus: float = 16.67
velocidad_moto: float = 19.44
# Ubicaciones del wifi (utilizado para el reto 4)
ubicaciones: list = [
    [6.211, -72.482, 2],
    [6.212, -72.470, 25],
    [6.105, -72.342, 25],
    [6.210, -72.442, 50]
]

'''
Variable para el reto 5, diccionario con la siguiente estructura:
{
‘actual’: [‘latitud’, ‘longitud’],
‘zonawifi1’: [‘latitud’, ‘longitud’, usuarios]
‘recorrido: [‘distancia’, ‘mediotransporte’,
‘tiempopromedio’]
}
'''
informacion_recorrido: dict = dict()

# Función para calcular distancia, recibe como parámetro una tupla con dos sub-tuplas
# con los siguientes datos ((lat1, lng1), (lat2, lng2)) --> (punto inicial, punto final)


def calcular_distancia(puntos: tuple):
    # Extraigo las tuplas internas que corresponde al punto inicio y punto final
    punto_ini, punto_fin = puntos
    # punto_ini: tuple = puntos[0]
    # punto_fin: tuple = puntos[1]
    dif_lat: float = punto_fin[0] - punto_ini[0]
    dif_lng: float = punto_fin[1] - punto_ini[1]
    # Aplica raíz cuadrada de la fórmula
    raiz: float = math.sqrt(math.pow(math.sin(math.radians(dif_lat/2)), 2) + math.cos(math.radians(
        punto_ini[0])) * math.cos(math.radians(punto_fin[0])) * math.pow(math.sin(math.radians(dif_lng/2)), 2))
    # Obtiene la distancia aplicando el restante de la fórmula
    distancia: float = 2 * R * math.asin(raiz)
    # retorna la distancia
    return distancia

# Función para validar que las ubicaciones que están dentro de la matriz
# estén dentro del rango especificado


def validar_matriz_ubicaciones():
    for m in ubicaciones:
        band_rango = validar_coordenadas(m[0], m[1])
        if not band_rango:
            print("Error")
            exit()

# Función para ubicar las zonas wifi mas cercanas


def ubicar_zonas_cercanas():
    os.system('clear')
    if len(coordenadas) > 0:
        cont: int = 1
        # Itera las coordenadas guardadas por el usuario
        for c in coordenadas:
            print(f"Coordenada [latitud, longitud] {cont} : [{c[0]}, {c[1]}]")
        # Solicita la ubicación actual al usuario
        opc: int = int(input(
            "Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: "))
        # Valida la opción ingresada
        if opc >= 1 and opc <= 3:
            # Obtiene la coordenada seleccionada por el usuario
            ubicacion_actual: list = coordenadas[opc-1]
            # Actualizacion para reto 5
            informacion_recorrido["actual"] = ubicacion_actual
            # Lista para almacenar todas las distancias y las coordenadas de los puntos de conexión
            # [ (distancia, [lat, lng, cant_personas]), ... ]
            distancias: list = []
            for u in ubicaciones:
                punto_ini: tuple = tuple(ubicacion_actual)
                punto_fin: tuple = tuple(u)
                # Calcula la distancia entre los puntos y los almacena en la lista
                item: tuple = (calcular_distancia(
                    (punto_ini, punto_fin)), punto_fin)
                distancias.append(item)
            # Ordena la lista de menor a mayor
            distancias.sort()
            # Envía los primeros dos items (las dos ubicaciones con menor distancia/las mas cercanas) y la ubicación actual
            mostrar_zonas(distancias[0], distancias[1], punto_ini)
        else:
            print("Error ubicación")
            exit()
    else:
        print("Error sin registro de coordenadas")
        exit()

# Función para mostrar zonas a partir de dos puntos (coordenadas)
# recibe como parámetro dos tuplas con la siguiente estructura: (distancia, [lat, lng, cant_personas])


def mostrar_zonas(punto_1: tuple, punto_2: tuple, ubicacion_actual: tuple):
    # Bloque para reordenar los puntos de menor cantidad de usuario a mayor cantidad de usuarios
    aux: tuple = punto_1
    if punto_1 > punto_2:
        punto_1 = punto_2
        punto_2 = aux
    print("Zonas wifi cercanas con menos usuarios")
    zona: list = [punto_1[1][0], punto_1[1][1]]
    distancia: float = punto_1[0]
    cant_personas: int = punto_1[1][2]
    print("La zona wifi 1: ubicada en ['{}', '{}'] a {} metros, tiene en promedio {} usuarios".format(
        zona[0], zona[1], distancia, cant_personas))
    zona: list = [punto_2[1][0], punto_1[1][1]]
    distancia: float = punto_2[0]
    cant_personas: int = punto_2[1][2]
    print("La zona wifi 2: ubicada en ['{}', '{}'] a {} metros, tiene en promedio {} usuarios".format(
        zona[0], zona[1], distancia, cant_personas))
    print("Elija 1 o 2 para escribir indicaciones de llegada")
    opc: int = int(input())
    # Valida la opción digitada
    if opc == 1:
        mostrar_indicaciones(punto_1, ubicacion_actual)
    elif opc == 2:
        mostrar_indicaciones(punto_2, ubicacion_actual)
    else:
        print("Error zona wifi")
        exit()

# Recibe como parametro una tupla con la información de la zona a indicar
# la tupla debe tener la siguiente estructura: (distancia, [lat, lng, cant_personas])


def mostrar_indicaciones(zona: tuple, ubicacion_Actual: tuple):
    # Obtiene datos de la tupla zona
    lat: float = zona[1][0]
    lng: float = zona[1][1]
    cant_personas = zona[1][2]
    distancia: float = zona[0]
    # Almacena los datos en la variable global para el reto 5
    informacion_recorrido["zonawifi1"] = [lat, lng, cant_personas]
    '''
    Plano cartesiano para los puntos cardenales (la posición inicial es la ubicación del usuario)
            y(lat) norte
              |
      (lng)   |
        x --------- oriente
              |
              |
             sur
    '''
    y: int = ubicacion_Actual[0]
    x: int = ubicacion_Actual[1]
    # Obtiene el tiempo promedio de transporte
    tiempo_bus: float = distancia / velocidad_bus
    tiempo_moto: float = distancia / velocidad_moto
    # Muestra información del tiempo de llegada al usuario
    print(f"El tiempo promedio en Bus es: {tiempo_bus}")
    print(f"El tiempo promedio en Moto es: {tiempo_moto}")

    # Puntos cardenales
    punto_cardenal_1: str = ""  # norte o sur
    punto_cardenal_2: str = ""  # oriente u oeste
    if lat > y:
        punto_cardenal_1 = "Norte"
    else:
        punto_cardenal_1 = "Sur"
    if lng > x:
        punto_cardenal_2 = "Oriente"
    else:
        punto_cardenal_2 = "Occidente"
    # Muestra indicaciones
    print(
        f"Para llegar a la zona wifi debe dirigirse primero al {punto_cardenal_1} y luego hacia el {punto_cardenal_2}")
    # Almacena la información de recorrido
    informacion_recorrido["recorrido"] = [distancia, "Bus", tiempo_bus]
    # Regresar al menú
    opc: int = int(input("Presione 0 para salir"))
    if opc == 0:
        funcion_reto2()
    else:
        print("Error")
        exit()


"""
=============FUNCIONES DEL RETO 5 ==================
"""
"""
=================================================================
===================VARIABLES GLOBALES RETO 5=====================
=================================================================
"""


def guardar_archivo():
    # Verifica que el usuario haya ingresado las coordenadas de los sitios frecuentes y el sitio actual
    if len(coordenadas) == 0 or len(informacion_recorrido) == 0:
        print("Error de alistamiento")
        exit()
    else:
        # Mostrar el diccionario
        print(informacion_recorrido)
        opc: int = int(input(
            "Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal "))
        if opc == 1:
            print("Exportando archivo")
            try:
                with open("informacion_recorrido.json", "w") as archivo:
                    json.dump(informacion_recorrido, archivo)
                    exit()
            except:
                print("Error")
                exit()


def actualizar_zonas_wifi():
    try:
        global ubicaciones
        archivo = open("coordenadas.txt")
        ubicaciones = eval(archivo.read())        
    except FileNotFoundError:
        print("No se encontró el archivo para actualizar las coordenadas")
    opc: int = int(input("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal "))
    if opc == 0:
        funcion_reto2()
    else:
        print("Error")
        exit()
"""
=============FUNCION PRINCIPAL DEL PROGRAMA ==================
"""


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
# funcion_reto2()
