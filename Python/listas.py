"""
#Lista con diferentes tipos de datos
lista: list = [5,2,"hola", True, 4.5]
#Añadimos un elemento a la lista
lista.append(10)
#Insertamos un elemento en la posición 0
#lista.insert(posición, valor_a_añadir)
lista.insert(0,8)
#Mostrar toda la lista
print(lista)

#Eliminar el último elemento
elemento_borrado = lista.pop()
print(lista)
print("El elemento eliminado es: ", elemento_borrado)
#Eliminar un elemento en un posición en específico
elemento_borrado = lista.pop(1)
print(lista)
print("El elemento eliminado es: ", elemento_borrado)
#reemplazar un elemento de la lista
lista[2] = "Fresa"
print(lista)
"""

