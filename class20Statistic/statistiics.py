import statistics
import csv
#Vamos a crear codigo que solamnte me muestre los ventas, la cantidasd de ventas

caja_de_numeros = {}
with open('class20Statistic/ventas.csv', mode='r') as file:
    verificacion = csv.DictReader(file)
    for row in verificacion:
        month = row['month']
        sales = int(row['sales'])
        caja_de_numeros[month]= sales

ventas =list(caja_de_numeros.values())
print(ventas)
#De esdta manera solamente me muestra los valores de ventas de cada mes

#Ahora vamos a encontrar la media, utilizando statistics.mean()

media = statistics.mean(ventas)
print(f"La media es : {media}")

#Ahora vamos a encontrar la mediana, utilizando statistics.median()

mediana = statistics.median(ventas)
print(f"La mediana es : {mediana}")


#Ahora vamos a encontrar la moda, utilizando statistics.mode()

moda = statistics.mode(ventas)
print(f"La moda es : {moda}")

#Ahora vamos a encontrar la desviación estandar, utilizando statistics.stdev()

mediacion_estandar = statistics.stdev(ventas)
print(f"La desviacion estandar es : {mediacion_estandar}")

#Ahora vamos a encontrar la varianza, utilizando statistics.variance()

varianza = statistics.variance(ventas)
print(f"La media es : {varianza}")

max_ventas= max(ventas)
min_ventas = min(ventas)

rango_de_venbtas = max_ventas - min_ventas
print(f"El rango de ventas es: {rango_de_venbtas}")