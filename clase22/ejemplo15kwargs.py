def imprimir_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

imprimir_info(name="Carlos", edad=23, ciudad="Bogota ")
imprimir_info(name="Brandon", edad=26, ciudad="Boyacá", pais="Colombia")

#Estre Kwargs se utiliza cuando no sabemos cuantosa argumentos va a tener esta funcion pero si sabemos que los argumentos d¿tendtran un nombre y un valor o una llave y ub valkor de esa llave, así que por eso se utilizan dos **