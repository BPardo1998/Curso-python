class Calcular:
#Con este decorador no estamos accediendo a infomeacion de la clase o del objeto, soelmante sirve para ordenar un metodo dentro de una clase, pero no accede a información de ningun tipo 
    @staticmethod
    def ejemplo(a : int, b : int) -> int:
        return a + b

#En este utilizamos otro decorador, el cual si accede a información y tambien nos indica que estamos trabajando no con el metodo sobre el cual esta, sino que estamos trabajando con toda la clase 
class Contar:
    count = 0

    @classmethod
    def incrementar(cls):
        cls.count += 1


Contar.incrementar()
Contar.incrementar()

print(Contar.count)
#Aqui retornamos el valor count que esta dentro de la clase Contar 


class Circle:
    def __init__(self, radius : float):
        self._radius = radius

    @property
    def area(self) -> float:
        return 3.1416 * (self._radius **2)
    
    @property
    def radio(self) -> float:
        return self._radius
    
    @radio.setter
    def radio(self, valor : float):
        if valor < 0:
            raise ValueError("No puede ser 0 o menor ")
        self._radius = valor

circulo = Circle(8)
print(circulo.radio)