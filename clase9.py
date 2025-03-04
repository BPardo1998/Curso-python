def naturales (n):
    if n < 1:
        return 0
    else:
        return n + naturales(n-1)

number = 8
print(f"La sumatoria de los números naturales hasta {number} es: {naturales(number)}")
     

try:
    divisor=int(input("Ingrese el numero divisor: "))
    dividendo=int(input("Ingrese el numero dividendo: "))
    result =divisor/dividendo
    print(result)
except ValueError:
    print("aqui debes colocar un  numero : ")
except ZeroDivisionError:
    print("no puedes dividir por 0")



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def saludar(self):
        print(f"Hola, soy {self.name} y tengo {self.age} años de edad")

persona1 = Person("Brandon", 27)

persona1.saludar()

class Banco:
    def __init__(self, cuenta, balance):
        self.cuenta = cuenta
        self.balance = balance
        self.esta_activa= True

    def deposito(self, valor):
        if self.esta_activa:
            self.balance += valor
            print(f"Haz echo un deposito de {valor}, tu nuevo saldo es {self.balance}")
        else:
            print("Debes corregir, Cuenta inactiva")

    def retiro(self, valor):
        if self.esta_activa:
            if valor <= self.balance:
                self.balance -= valor
                print(f"Haz echo un retiro de {valor}, tu nuevo saldo en la cuenta es de {self.balance} pesos")

    def Cuuenta_desactivada(self):
        self.esta_activa = False
        print(f"La cuenta esta deesactivada")

    def Cuenta_Activada(self):
        self.esta_activada = True
        print(f"La cuenta esta activada nuevamente")

cuenta1 = Banco("Brandon", 4000)

cuenta21 = Banco("Ana", 1000)

cuenta1.deposito(2000)
cuenta21.deposito(9000)
cuenta21.Cuuenta_desactivada()
cuenta21.deposito(1000)
