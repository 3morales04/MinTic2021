"""Reto 1: Primera etapa del proyecto TicNet"""

# Mensaje de Bienvenida
def mensajeBienvenida() -> str:

    print("\n Bienvenido al sistema de ubicación para zonas públicas WIFI \n")

# Validacion de credenciales
def credenciales() -> str:
#Datos predefinidos
    usuario: str = "51630"
    contrasena: str = "03615"

#Validaciones de credenciales
    usuarioIngresado: str = input(" Nombre de Usuario: ")
    if usuario == usuarioIngresado:
        contrasenaIngresado: str = input(" Contraseña: ")
        if contrasena == contrasenaIngresado:

            #Calculos aritmeticos
            try:
                ultimosDigitos: int = 630
                numPenultimo: int = 3
                operacion: int = (6*5)/((6+5)-1) 
                if numPenultimo == operacion:
                    valorCaptcha: int = ultimosDigitos + numPenultimo
                    respuestaCaptcha = int(input(f" {ultimosDigitos} + {numPenultimo} = "))
                    
                    #Validacion Captcha de seguridad
                    if valorCaptcha == respuestaCaptcha:
                        print(" \n Sesión iniciada \n")
                    else:
                        print("\n Error")
                else:
                    print("\n Error")     
            except:
                print("\n Error")
        else:
            print("\n Error")
    else:
        print("\n Error")

#Se invoca las funciones
mensajeBienvenida()
credenciales()