
diccionario_persona = {
    "nombre": "Juan",
    "apellido": "Herrera",
    "edad": 25,
    "estudiante": True,
    "sueldo": 10.5,
    "ventas": {
        "enero":{
            "lunes": 10,
            "martes": 22
        },
        "febrero":{
            "lunes": 12,
            "martes": 30
        }
    }
}

#Recorrer directamente los valores de un diccionario
for x in diccionario_persona.values():
    print(x)

#Recorrer los items de un diccionario
for clave, valor in diccionario_persona.items():
    print("clave: ", clave)
    print("valor: ", valor)

"""
Desempaquetando tuplas
tupla = (1,2)
print(tupla)
num1, num2 = tupla
print(num1)
print(num2)
"""
