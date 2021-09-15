
print("Qué género musical te gusta?" , "\n Ingrese 1 para un si o un 0 para un No.")


try:
    Reggaeton = int(input("Reggaeton: "))
    Salsa= int(input("Salsa: "))
    Bachata = int(input("Bachata: "))
    
except:
    print("Recuerda que se ingresa 1 o 0 de acuerdo a tus gustos")

if Reggaeton == 1:
    print("Escucha Si veo a tu mamá - Bad Bunny")
elif Reggaeton == 0:
    print()
else:
    print ("Recuerda que se ingresa 1 o 0 de acuerdo a tus gustos")

if Salsa == 1:
    print("Escucha Deseándote - Frankie Ruiz")
elif Salsa == 0:
    print()
else:
    print ("Recuerda que se ingresa 1 o 0 de acuerdo a tus gustos")

if Bachata == 1:
    print("Escucha El perdedor - Aventura")
elif Bachata == 0:
    print()
else:
    print ("Recuerda que se ingresa 1 o 0 de acuerdo a tus gustos")