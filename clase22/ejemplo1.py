def division(num1 : int, num2 : int) -> float:

    if not isinstance(num1, int) or not isinstance(num2, int):
        print("Hambois parametros deber ser numeros enteros o flotantes")
        return None
    if num2 == 0:
        print("El numero divisor no debe ser 0")
        return None
    
    return num1/num2

uno = division(324, 61)
print(uno)