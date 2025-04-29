#Decopradores en python

def transaccción(func):
    def envolver():
        print("1 Carfando la transaccion....")
        func()
        print("3 Transaccion terminada ")
    return envolver


@transaccción
def pago():
    print("2 Porcesando el pago")

pago()

#Pago se combierte en el parametro de la variable transaccion y actua como funcion, entonmces cuando ejecyutamos, pasa a ser el parametro de trabnsaccion y cuando se ejecuta transaccion, devuelve la variable envoolver y muestra el primer print, luego dfe esto, se ejecuta el seghundo print, ya que llama ala funcion que en estecaso es la variable pago y se ejecuta l avariable pago y devuelve el sehundo print, al termino devuuelve el tercer print