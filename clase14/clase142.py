
#El bloque de código dentro del with garantiza que el recurso se "cierre" automáticamente cuando se termina de usar, incluso si ocurre algún error dentro del bloque. Esto es especialmente útil con archivos, porque asegura que el archivo se cierre cuando ya no se necesita.

#LEER UN ARCHIVO LINEA POR LINEA
"""with open('clase14/caperucita.txt','r') as file:
    for lineas in file:
        print(lineas.strip())
"""
#Función incorporada en Python que se usa para abrir un archivo. Toma dos parámetros principales:El primero es el nombre del archivo o la ruta del archivo. En este caso, 'caperucita.txt'.El segundo parámetro es el modo de apertura del archivo. 'r' significa modo lectura (read), lo que indica que el archivo solo se va a leer, no se va a modificar.'r':

#strip() es un método de las cadenas de texto (strings) en Python. El propósito de este método es eliminar los caracteres en blanco al principio y al final de la cadena de texto. Esto incluye espacios, saltos de línea, tabulaciones, etc. Se usa para limpiar las líneas de texto antes de mostrarlas o procesarlas.

#LEER solo la primer linea del archivo
"""with open('clase14/caperucita.txt','r') as file:
    lineas = file.readline()
    print(lineas)"""
#
with open('clase14/caperucita.txt','a') as file:
    file.write("\n\n\n\nEsta es la mejor histioria ")