import os
os.system('clear')

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
def menu(listamenu):
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
    return opmenu

def opcion_6(listamenu): # se hace el intercambio de las opciones del menu.
    opfavorita = int(input("Seleccione opción favorita: "))
    if (opfavorita >= 1 and opfavorita <=5):
        adv = int(input("Para confirmar por favor responda: Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es "))
        if (adv == 9):
            adv2 = int(input("Para confirmar por favor responda: De millones de hijos que somos el primero nací, pero aun así soy el menor de todos. ¿Quién soy? : "))
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

def funcion_reto2(listamenu):
    # Sub programa 
    contint = 0 # cuenta el numero de intens fallido y se sale del menu al ser igual a 3
    opmenu = 1 # se inicializa en 1 para que entre por primera vez al while
    # ciclo repetitivo para controlar el menu
    while (opmenu != 7 and contint !=3): 
        opmenu = menu(listamenu)
        if (opmenu > 7) or (opmenu <= 0): # controlo que las opciones del menu esten entre 1 y 7
            contint +=1
            print("Error")

        if opmenu == 1:
            print(f"Usted ha elegido la opción {opmenu}") 
            exit()
        
        if opmenu == 2:
            print(f"Usted ha elegido la opción {opmenu}") 
            exit()

        if opmenu == 3:
            print(f"Usted ha elegido la opción {opmenu}") 
            exit()

        if opmenu == 4:
            print(f"Usted ha elegido la opción {opmenu}") 
            exit()
        
        if opmenu == 5:
            print(f"Usted ha elegido la opción {opmenu}") 
            exit()

        if opmenu == 6: 
            opmenu = opcion_6(listamenu) 
            os.system('cls')

        if (opmenu == 7):
            print("Hasta pronto")
            exit()
        


# Programa Principal
def main():
    """
    -------------------Bloque de código del reto 1 ---------------------------
    """
    print('Bienvenido al sistema de ubicación para zonas públicas WIFI') 
    try:
        usuario=51630
        password = '03615'
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
                    #Crea lista de opciones
                    listamenu = ["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo","Elegir opción de menú favorita","Cerrar sesión"]                                   
                    #Llama a la función del reto 2
                    funcion_reto2(listamenu)                                                      
                else:
                    print("Error")                                              
                    exit()
            else:
                print("Error")                                               
                exit()   
    except:
        print("Error")

#Llamar a la función principal de mi programa
main()
