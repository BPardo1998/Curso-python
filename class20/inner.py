x = 'global' #Variable global

def funtion_one():
    x = 'one'
    def funtion_two():
        x = 'two'
        print(x) #Mandamos llamar el valor de funtion_two

    funtion_two()#Aqwui se termina de ejecutar la funcion 
    print(x)#Mandamos llamar el valor de la funtion_one

funtion_one()#Aqui se termina de ejecutar la funcion 
print(x)#Ya llamamos todo, ahora llamamos la variable global