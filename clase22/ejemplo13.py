class Multyfactor:


    def __new__(cls, factor : int):
        print(f"Creando instancia con factor {factor}")
        return super(Multyfactor, cls).__new__(cls)

    def __init__(self, factor : int):
        print(f"Inicializando con factor {factor}")
        self.factor = factor
    
    def __call__(self, number : int) -> int:
        return number * self.factor
    
multiplicación = Multyfactor(5)

result= multiplicación(10)
print(result)
        