def sumar(a, b, c, d):  
    return a + b + c + d

valor = (1, 4, 5, 12)
print(sumar(*valor))
#Aqui recibimos los args


def ejemplo(nombre, edad):
    print(f"Este es el nombre: {nombre} y su edad es: {edad}")

argumentos = {"nombre": "Brandon", "edad": 32 }
print(ejemplo(**argumentos))
#Aqui recibimos los kwargs 