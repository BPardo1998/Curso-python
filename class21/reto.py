#Recibir una lista de diccionarios y cada diccionario debe tener nombre, edad y sueldo 

lista = [
     {
        "nombre" : 'juan',
        "edad" : 56,
        "sueldo" : 34456
    },
     {
        "nombre" : 'pedro',
        "edad" : 56,
        "sueldo" : 45675
    },
   {
        "nombre" :'Ruth',
        "edad" : 34,
        "sueldo" : 58888
    }
]

#Devolñver una lista conb empleados que tengas un sueldo menor e igual a 40000

def minimo (lista):
        return [empleado for empleado in lista if empleado["sueldo"] <= 40000]

print(minimo(lista))
