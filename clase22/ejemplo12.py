def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def divifir(a, b):
    if b == 0:
        raise ValueError(f"El valor del dividendo no de be ser 0 o negativo")
    return a / b

if __name__ == "__main__":
    print("Las operaciones son")
    resp1 = sumar(4, 8)
    print(f"La suma es : {resp1}")
    print(divifir(4,2))
    print(multiplicar(8, 10))
    print(restar(10, 2))


#Si queremos visualizar de manera directa desde la consola, debemos acceder a la carpeta donde esta el docuemnto y cuando estemos situados sobre y dentro de la carpeta donde esta el archivo.py, }escribimos el siguiente codigo python "el nombre del archivo.py" donde esta nuestra codigo, de esta manera se muestra completamente y de forma automatica el arechivo 