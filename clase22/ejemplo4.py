from collections import deque

def lista_de_espera() -> deque:
    lista =deque(["orden1", "orden2", "orden3"])
    lista.append("lista4") #Agregar esto al final de la lista
    lista.appendleft("lista0") #Agrega al inicio de la lista
    lista.pop()#Elimina el ultimo
    lista.popleft()#Eñlimina el porimero

    return lista

gestion = lista_de_espera()
print(gestion)