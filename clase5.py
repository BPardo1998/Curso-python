numeros= [i**2 for i in range(1,10)]
#print(f"Los numeros elevados al cuadredo son{numeros}")


Celsius= [0, 10, 20,30,40,42]
fahrenheit = [(temp * 9/5) + 32 for temp in Celsius]
#print(f"La temperatura en grafos F es {fahrenheit}")

pares = [i for i in range(1,21) if i%2 == 0]
#print(pares)
#pares = [i for i in range(1,21) if i%2 == 1]
#print(pares)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
#1Primero con [fila[i] for fila in matrixrecorre cada fila encontrando los i de cada fila,
#2 con range(len(matrix[0])) encuentra que la longitud de la fila 0 es de tres, lo que hace que halla un i=0 un i=1 y un i=2, y cada uno de estos sera una columna que luego que comvertira en una nueva fila.
#3, ya sabiendo cuales son las columnas, con for i in range(len(matrix[0]))crea las nuvas filas que son las anteriores columnas, dando como resultado la tranformación TRANSPONER
transponer = [[fila[i] for fila in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transponer)
print(type(transponer))



