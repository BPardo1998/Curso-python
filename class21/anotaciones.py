class Persona:
    name : str
    edad : int
    sueldo : float

    def __init__(self, name : str, edad : int, sueldo : float):
        self.name = name
        self.edad = edad
        self.sueldo = sueldo
        
    def presentacion(self)-> str:
        return f"Hola, soy {self.name}, tengo {self.edad} y actualmente trabahjo y gano {self.sueldo} de pesos al mes"
    
persona1 = Persona('Brandon', 28, 234765.87)
print(persona1.presentacion())
