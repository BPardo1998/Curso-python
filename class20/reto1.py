#Reto, crear dos funciones, la primera recibe un diccionario con informacion de clientes y la segunda me muestra qu eclientes tienen un sueldo en especifico 

empleados = {
    "empleado1": {
        "nombre": "Carlos",
        "edad": 28,
        "salario": 3500
    },
    "empleado2": {
        "nombre": "Laura",
        "edad": 34,
        "salario": 4200
    },
    "empleado3": {
        "nombre": "Miguel",
        "edad": 45,
        "salario": 5000
    }
}

salario_minimo = [empleado for empleado, datos in empleados.items() if datos["salario"] >= 4000]
print(salario_minimo)

#En el bucle, empleado recibe el nombre de la clave que es empleado1 o el 2 o el 3 y dato recibe la informacion que contiene cada clave, como nombre edad y salario y EMPLEADOS.ITEMS() recibe las dos cosasa al tiempo

salario_minimo = [datos["nombre"] for empleado, datos in empleados.items() if datos["salario"] >= 4000]
print(salario_minimo)



