from collections import defaultdict
#Defaultdict es un diccionario de  la libreria Colllection y lo que hace es que si accede a una clave que no exixtte, este devuelve un valor por defecto
def contar_roductos(orden: list[str]) -> defaultdict:
#Creamos una variabvle que va a hacer un defaultdict que cuando coloco (int), este me devolvera0, indicando que el contador inicia desde 0
    contador = defaultdict(int)
    for product in orden:
        contador[product] +=1
#Cuando contador encuentre un producto igual despues de cada iteración, va a sumar cuantas veces lo encuentre
    return contador

orden = ['papel', 'computador', 'papel', 'esfero']
caja = contar_roductos(orden)
print(caja)