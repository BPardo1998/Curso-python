numeros = [1,2,3,4,5,6,7,8]
for i in numeros:
    print("este es eñllñ numero", i)

for i in range(12):
    print(i)
    if i == 6:
        print("Enconre el numero 6")

numeros = [1,2,3,4,5,6,7,8]
for i in numeros:
    if i == 5:
        continue
    print("este es eñllñ numero")

#para hacer una iteración, rimero debo crear un afuncion donde se va a guardar la iteración y debo utilizar la palabra clave iter y ahi meter mi lista que vboy a iterar
iterarc = iter(numeros)

#Luego mando llamar mi iiterqaci´pon y tulizo la palabra clave next para devolver de uno a uno cada elemnto de mi lista, iniciando con ell primero 
print(next(iterarc))


texto = "Hola querida"

itertext = iter(texto)
#aqui estam,os iterando un texto y utilizamos un for, opero tambi9en como es texto utilizamos la palabra clave char que significa palabra
for char in itertext:
    print(char)


numeritos = 11

numiter = iter(range(2, numeritos+4,3))

for num in numiter:
    print(num)



