class Vehiculos:
    def __init__(self, nombre, modelo, precio):
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
            
