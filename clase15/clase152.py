import csv 
#Coje un listado de prooductos y los ordena, por nombre, precio y cada unode los objetos que tiene esta lista 
with open('clase15/nota.csv', 'r') as file:
# kuego creamos una variable que sera la cahja deonde se va aguardar esta nueva información oordenada, y atraves de DictRead, devuelkve y se guarda cada linea pero en modo diccionario, estructura que guarda clave y valor de file, que es la caroppeta donde esta la información 
    caja = csv.DictReader(file)
#Aqui vamos a utiolizar el bucle for y para cada fila dentro de caja que es donde esta guardada la nueva informacion, vamos a delver solamnte fila por fila horizontal
    for row in caja:
#aqui se reflejan las filas una por una en modo diccionario con su clave y valor 
        print(row)

with open('clase15/nota.csv', 'r') as file:
     caja = csv.DictReader(file)
     for row in caja:
         print(f"Producto : {row['name']}, Costo: {row['price']}")

#Vamos a creear una nueva fila con un producto nuevo en nuestro archivo csv

import csv

new_product = {
    'name': 'cargador portatil',
    'price': 7500,
    'quantity': 190,
    'brand': 'Cargadores',
    'category': 'Accesortios',
    'Fecha': '09-08-2025',
}
with open('clase15/nota.csv', mode='a', newline='') as file:
    #file.write('\n')
    libreria = csv.DictWriter(file, fieldnames = new_product.keys())
    #fieldname signifrica que es el quie me encuentra los nombres de las columnas o llamadas llaves 
    libreria.writerow(new_product)
