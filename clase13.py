class Servivo:
    def __init__(self, name):
        self.name = name

class Persona(Servivo):
    def __init__(self,  name, edad):
        super().__init__(name)
        self.edad = edad

class Estudiante(Persona):
    def __init__(self,  name, edad, identificación):
       super().__init__(name, edad)
       self.identificación = identificación

    def presente(self):
        print(f"Hola, mi nombre es {self.name}, tengo {self.edad} y ni munero de identificación es {self.identificación}")

estudiante1 = Estudiante("Brandon", 28, "2354925492363")

estudiante1.presente()