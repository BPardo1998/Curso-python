class Persona:
    def __init__(self, nombre : str, edad : int):
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str :
        return f'Persona: {self.nombre}, {self.edad} años'
    #Aqui devuelve una cdena de texto con la información de nommbre y edad al usuario
    
    def __repr__(self) -> str:
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    #Aqui devuelve una información clara especificando cual es el nombre y edad al usuario
    
    def __eq__(self, otra_person) -> bool:
        return self.nombre == otra_person.nombre and self.edad == otra_person.edad
    #Aqui compara si el nombre y edad de persona es igual a el nombre y edad de la nueva persona de otra_person y arroja y resultado tipo true o folse, por ser booleano

    def __lt__(self, otra_person):
        return self.edad < otra_person.edad
    #Aqui podemo0s comparar que persona es menor que otra con respecto a la edad 

    def __le__(self, other):
        return self.edad <= other.edad
    
    def __add__(self, other):
        return self.edad + other.edad
    


# Aqui se crean las instancias de personas
P1 = Persona("Brandon", 26)
P2 = Persona("Aleja", 27)
P3 = Persona("Ruth", 34)

print(str(P2))
print(repr(P1))
print(P2 == P1)
print(P2 < P3)
print(P2 <= P3)
print(P2 + P3)



