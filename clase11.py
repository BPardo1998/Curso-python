class Carros:
    def __init__(self, nombre, modelo, color):
        self.nombre = nombre
        self.modelo = modelo
        self.color = color
        self.disponible= True   

    def comprar(self):
        if self.disponible:
            self.disponible = False
            print(f"El {self.nombre}, modelo {self.modelo}, del color {self.color} ya fue vendido, te estaremm,ops avisando si tenemos mas existencias") 
        else:
            print(f"El {self.nombre}, modelo {self.modelo}, del color {self.color}, no esta disponible")  

    def vender(self):
        self.disponible = True
        print(f"El {self.nombre}, fue adquirido de nuevo por la concecionaria, se encuentra listop para vender, es modelo {self.modelo}, de color {self.color}")  

class Usuario:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.historial = []
    
    def comprar_carro(self, nombre):
        if nombre.disponible:
            nombre.comprar()
            self.historial.append(nombre)
        else:
            print(f"El vehiculo {self.nombre}, no esta disponible para ser copmprado")

    def venderle_carro(self, nombre):
        if nombre in self.historial:
            nombre.vender()
            self.historial.remove(nombre)
        else:
            print(f"El vehivculo {self.nombre}, no cumple con nuestras politicas, no te lo podemos comprar") 

class Concesionario:
    def __init__(self):
        self.lote_de_carros = []
        self.usuarios = []

    def carros_nuevos(self, nombre):
        self.lote_de_carros.append(nombre)
        print(f" Se a agregado el {nombre.nombre}, al lote de carros listo para vener")

    def nuevo_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Haz agregado el asuario {usuario.nombre} a nuestra base de datos")

    def carros_disponibles(self):
        print("Carros disponibles")
        for nombre in self.lote_de_carros:
            if nombre.disponible:
                print(f"Tu carro {nombre.nombre}, de modelo {nombre.modelo}, de color {nombre.color}, esta disponible para qu elo compres")

carro1 = Carros("Suzuky hidrido", "2024", "azul con blano")
carro2 = Carros("escarabajo", "2012", "blano")
carro3 = Carros("toyota", "2024", "azul")
carro4 = Carros("nissan", "2000", "gris")
carro5 = Carros("chevrolet", "2003", "amarillo")

usuario11 = Usuario("Brandon", "0001")
usuario22 = Usuario("Ginna", "0002")
usuario33 = Usuario("Franck", "0003")

Compraventa = Concesionario()
Compraventa.carros_nuevos(carro1)
Compraventa.carros_nuevos(carro2)
Compraventa.carros_nuevos(carro3)
Compraventa.carros_nuevos(carro4)
Compraventa.carros_nuevos(carro5)
Compraventa.nuevo_usuario(usuario11)
Compraventa.nuevo_usuario(usuario22)
Compraventa.nuevo_usuario(usuario33)

Compraventa.carros_disponibles()

usuario22.comprar_carro(carro4)
usuario33.comprar_carro(carro1)
usuario33.comprar_carro(carro2)

Compraventa.carros_disponibles()

usuario33.venderle_carro(carro1)

Compraventa.carros_disponibles()