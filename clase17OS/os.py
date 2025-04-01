import os

carpeta = os.getcwd()
print("El directoprio actual es: ", carpeta)

txt_carpeta = [f for f in os.listdir('.') if f.endswith('.txt')]
print("ASrchivos .txt existenntes son:", txt_carpeta)

#Se crea un avariable que esl aque vamos a iterar, por cada f que este en la lista con archivos y carpetas del directorio aen la clase 14 y si f termina en .txt, devuelveme y miuestrame todos los archiovos txt que encoinetrastey que sean guardados en la carpeta txt_carpeta.


txt_carpeta2 = []

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.txt'):
            # Agrega el archivo encontrado a la lista
            txt_carpeta2.append(os.path.join(root, file))

# Imprime los archivos .txt encontrados

print("ASrchivos .txt existenntes son:", txt_carpeta2)

#Aqui recorremos acrpetas dentro del directorio root, que es la ruta de la carpeta actual, dirs que es una lista de subcarpetas dentro de root y files que es la lista de archivos dentro del root y subcarpetas hasta encontrar todo lo que buscamos y se guarda en txt carpeta2