class Vehiculos:
    def __init__(self, nombre, modelo, precio):
        #Pilar No1  Encapsulación, las cuales son variables de isntancia que contie4nen datos proiovados del objeto
        self.nombre = nombre
        self.modelo = modelo
        self.precio = precio
        self.disponible = True

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f"El vehiculo {self.nombre} ya se vendio")
        else:
            print(f"El vehiculo {self.nombre} no esta disponible.")
             
    #Pilar No2 Abstracción  
    def estado(self):
        return self.disponible
#Queremos saber el precuiio de un vehioculo    
    def get_precio(self):
        return self.precio
#Los dos objetos de abajo, por si solos no devuelven nada, debemos crear una sub clase que erede la clase madfdre de arriba, y a esta subclase, crearle la infor,macion del metodo prender carro o apagar carro   
    def prender_vehiculo(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def apagar_vehiculo(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
#aqui vam,os a crear una subclase, que va aheredaar la clase Vehicuvlos. al colocar el not, hace referencia a que el carro ya no esta disponible por que fue vendido, entonces púedo porender el carro
#Pilar No3 Herencia
class Carro_particular(Vehiculos):
        def prender_vehiculo(self):
            if not self.disponible:
                return f"Has prendido el motor del {self.nombre}, no presenta novedades de funcionamiento"
            else:
                return f"El carro {self.nombre}, no esta disponible"
            
        def apagar_vehiculo(self):
            if self.disponible:
                return f"El motor del carro {self.nombre}, se apago"
            else:
                return f"El carro {self.nombre}, no esta disponible"

class Motocicleta(Vehiculos):
    def prender_vehiculo(self):
            if not self.disponible:
                return f"Has prendido el motor de la {self.nombre}, no presenta novedades de funcionamiento"
            else:
                return f"La moto {self.nombre}, no esta disponible"
            
    def apagar_vehiculo(self):
            if self.disponible:
                return f"El motor de la motocicleta {self.nombre}, se apago"
            else:
                return f"La moto {self.nombre}, no esta disponible"
class Camion(Vehiculos):
    def prender_vehiculo(self):
            if not self.disponible:
                return f"Has prendido el motor del camion {self.nombre}, no presenta novedades de funcionamiento"
            else:
                return f"El camion {self.nombre}, no esta disponible"
            
    def apagar_vehiculo(self):
            if self.disponible:
                return f"El motor del camion {self.nombre}, se apago"
            else:
                return f"El camion {self.nombre}, no esta disponible"

class Comprador:
    def __init__(self, compradorr):
          self.comprador = compradorr
          self.historial = []

    def comprar_vehiculo(self, vehiculo: Vehiculos):
        if vehiculo.estado():
              vehiculo.vender()
              self.historial.append(vehiculo)
        else:
             print(f"El vehiculo {vehiculo.nombre}, no esta diponible, pero hay muchos mas")

    def verificar_disponibilidad(self, vehiculo: Vehiculos):
        if vehiculo.estado():
            confirmacion = "Disponible"
        else:
            confirmacion = "No disponible"
        print(f"El vehiculo {vehiculo.nombre} esta {confirmacion} y tiene un costo de {vehiculo.precio}")

class Concesionario:
    def __init__(self):
          self.lote_de_carros = []
          self.compradores = []

    def añadir_carronuevo(self, vehiculo:Vehiculos):
         self.lote_de_carros.append(vehiculo)
         print(f"El vehiculo {vehiculo.nombre}, esta recien llegado al concecionario, sigfueme para poder concerlo")

    def añadir_usuario(self, comprador:Comprador):
         self.compradores.append(comprador)
         print(f"El nuevo cliente {comprador.compradorr}, se añadiop satisfactoriamente")

    def mostrar_carros_disponibles (self):
         print("Los carros dispónibles son:")
         for vehiculo in self.lote_de_carros:
              if vehiculo.estado():
                   print(f" El {vehiculo.nombre} .  que cuesta {vehiculo.get_precio()}")
                   
carro1 = Carro_particular("Suzuki", "2014", "$56.000.000")         
carro2 = Carro_particular("chevreolet", "2014", "$36.000.000") 
carro3 = Carro_particular("Toyota", "2014", "$256.000.000")
carro4 = Carro_particular("Bolvo", "2014", "$96.000.000")      
moto1 = Motocicleta("rex", "2014", "$6.000.000")             
moto2 = Motocicleta("auteco", "2014", "$12.000.000") 
camion1 = Camion("Pireli", "2014", "$212.000.000")
camion2 = Camion("Chevrolet", "2024", "$312.000.000")

comprador1 = Comprador("Brandon")

casa = Concesionario()
casa.añadir_carronuevo(carro1 )
casa.añadir_carronuevo(carro2 )
casa.añadir_carronuevo(carro3 )
casa.añadir_carronuevo(carro4 )
casa.añadir_carronuevo(moto1 )
casa.añadir_carronuevo(moto2 )
casa.añadir_carronuevo(camion1 )
casa.añadir_carronuevo(camion2 )

casa.mostrar_carros_disponibles()

comprador1.verificar_disponibilidad(carro4)


comprador1.comprar_vehiculo(carro4)

casa.mostrar_carros_disponibles()
