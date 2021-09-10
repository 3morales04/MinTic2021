
#Conjunto
conjunto = {"juan", "herrera"}
#Diccionarios
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

#Acceder al nombre de la persona
nombre: str = diccionario_persona["nombre"]
print(nombre)
#Acceder a las ventas de la persona
ventas = diccionario_persona["ventas"]
print(ventas)
enero = ventas["enero"]
print(enero)
martes = enero["martes"]
print(martes)
#ventas_lunes = ventas["lunes"]
#print(ventas_lunes)


estudiante: dict = {
    "nombre":"",
    "edad": 10,
    "fecha_nacimiento": "",
    "materias": [{"nombre":"", "facultad": ""}, {}]
}
