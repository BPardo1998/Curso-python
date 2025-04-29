# Creamos una lista de mercado, tambien una clase con estados y lo que queremos es que cuando agreguemops algo a mi carrito de esa lista de mercado, me mueste que se añadio y tanmbien un contador qu e me permita ver cuantas veces e añadido algpoo a mi carrito 

from collections import  deque, Counter
from enum import Enum

#Creamos la clase que recibe tres estados
class Estado(Enum):
    Añadido = 1
    Eliminado = 2
    Verificado = 3

#Creamos una lista de mercado

Mercado = ["Arroz", "Papa", "Panela!", "Arina", "Pan"]


#Creamos una lista que va a hacer un deque que esta vacia pero ahi se guardara lo que añadas
carrito = deque()

# Crweamos una funcion que cunado se valide el estado, dependiendo de cual sea, se añada un producto a la lsita vacia de arriba, o se limine o simplemente se verifique 
def mercar( estado : Estado, producto : str):
    if estado == Estado.Añadido:
        carrito.append(producto)
        return f"Añadiste {producto} al carrito"
    elif estado == Estado.Eliminado:
        if producto in carrito:
            carrito.remove(producto)
            return f"Eliminaste {producto} del carrito"
        else:
            return f"El {producto} no esta en el carrito"
    if estado == Estado.Verificado:
        if not producto in carrito:
            return f"Estas verificando el {producto} para meterlo al carrito"
        else:
            return "ya tienes el productoo en el carrito, quieres llevar otro igual ?"

#Creamos la funcion conmtador que devuelve el conteo de los elemntos dentro de carrito 
def contador ():
    return Counter(carrito)

#Como añadir el el producto al carrito 

print(mercar(Estado.Añadido, "Arroz"))
print(mercar(Estado.Añadido, "Papa"))
print(mercar(Estado.Añadido, "Arina"))
print(mercar(Estado.Añadido, "Pan"))
print(mercar(Estado.Verificado, "Arroz"))

print(mercar(Estado.Eliminado, "Pan"))

#Devolvemos la función qu eme muestra el conteo de cada elemento que hay en carrito
print(contador())



