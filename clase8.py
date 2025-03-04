#     

def suma(a,b):
    return a + b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division (a,b):
    return a/b

def calculadora():
    while True:
        print("Selecciones una operacion")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        option = input("Ingrese su opcion(1,2,3,4,5): ")

        
        if option in ["1","2","3","4"]:
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))    

            if option == "1":
                print("La suma es : ", suma(num1, num2))
            if option == "2":
                print("La resta es : ", resta(num1, num2))
            if option == "3":
                print("La multiplicación es : ", multiplicacion(num1, num2))
            if option == "4":
                print("La division es : ", division(num1, num2))
        if option == "5":
            print("saliste de la calculadora")
            break 
calculadora()