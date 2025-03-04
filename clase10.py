class Libro:
    def __init__(self, titulo, author):
        self.titulo = titulo
        self.author = author
        self.disponible = True

    def prestar (self):
        if self.disponible:
            self.disponible = False
            print(f"El libro {self.titulo} ha sido prestado, debes elejir otro")
        else:
            print(f"El libro {self.titulo} no esta disponible")

    def devolucion (self):
        self.disponible = True
        print(f"El libro {self.titulo}, ha sido devuelto, quieres llevartelo")
class User:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        #Aqui colocamos una lista donde se vana guardar todos los libros que le han prestado
        self.Libros_prestados = []

#Funcion para prestarnos un libro
    def prestamo(self, libro):
        # si el libro esta disponible
        if libro.disponible:
            #podemos prestarnos un libro, sa cambia el estado
            libro.prestar()
            #agregamos el libro prsestado a nuestra lista utiolizando append()
            self.Libros_prestados.append(libro)
        else:
            print(f"El libro{libro.titulo}, no esta disponible para ser prestado")

    def devolver(self, libro):
            if libro in self.Libros_prestados:
                libro.devolucion()
                self.Libros_prestados.remove(libro)
            else:
                print(f"El libro{libro.titulo}, no lo has pedido prestado, no lo tienes")

class Biblioteca:
    def __init__(self):
        self.ensiclopedia = []
        self.usuarioss = []
    
    def Agregar_libro(self, libro):
        self.ensiclopedia.append(libro)
        print(f"Haz agregado el libro {libro.titulo} a tu biblioteca")

    def Agregar_Usuario(self, usuario):
        self.usuarioss.append(usuario)
        print(f"Haz agregado el usuario {usuario.nombre} a tu biblioteca")

    def Libros_Disponibles(self):
        print("Libros disponibles")
        for libro in self.ensiclopedia:
            if libro.disponible:
                print(f"Tu libro{libro.titulo}, del autor{libro.author} esta disponible")


#crea,os los objetos 
#Creamos los libros 
libro1 = Libro("El club de las 5 am", "Robin Sharma")
libro2 = Libro("Hbitos atómicos", "James Cleare")

#Creamos los usuarios

usuario1 = User("Brandon", "0001")

#Creamos la biblioteca

libreria = Biblioteca()
libreria.Agregar_libro(libro1)
libreria.Agregar_libro(libro2)
libreria.Agregar_Usuario(usuario1)

#Mostrar lñobros

libreria.Libros_Disponibles()

#Se va a realizar un prestamo

usuario1.prestamo(libro1)

libreria.Libros_Disponibles()

#Se va a devolver un libro

usuario1.devolver(libro1)