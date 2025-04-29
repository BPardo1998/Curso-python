class Ejemplo:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.habilidades = args
        self.detalles = kwargs

    def ejecutar(self):
        print(f"Nombre: {self.name}")
        print("Habilidades :", self.habilidades) #Aqui me va amostrar una tupla con la infom4acion de los args
        print("Detalles :", self.detalles) #Aqui tenemos uin diccionario con los argumentos que se guardan con clave y valor

ejecutando = Ejemplo("Branmdon", "Especialización en grencioa de proyectos", "Ingeniero Naval", "Programador", edad=26, residencia = "Toca")
ejecutando.ejecutar()

#En la linea 9 y 10  lops self. no estan entre coprchetes debido a que al guardarse el tuplas() y en diccionarios[], ya ellos tienes cada uno en automatico llaves y cotchetes