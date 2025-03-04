name = "Brandon antonio"
saludo = "Hola, que tal"
pregunta = "A donde vas"
print(saludo + " " + name + " "+ pregunta)
print(saludo + " " + name + " "+ pregunta.casefold())
print(saludo, name, pregunta, sep=".. ")

print(f"Este es un saludo {saludo} va para {name} y te esta preguntando {pregunta.casefold()}")



nombre = input("Coloca tu edad aqui: ")
print(nombre)