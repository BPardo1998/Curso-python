import  csv

fila_original= 'clase15/nota.csv'
nueva_fila = 'clase15/nota_nueva.csv'

with open(fila_original, mode='r') as file:
    box = csv.DictReader(file)
    #Aqui obtenemos los nombres de las columnas existentes, para ello abrimos una lista y esta es sumada, dentro de la lista estara el valor total 
    fieldname = box.fieldnames +['valor_total']

    with open(nueva_fila, mode='w', newline='') as nueva_fila:
        box_write = csv.DictWriter(nueva_fila, fieldnames = fieldname)
        box_write.writeheader()

        for row in box:
            row['valor_total'] = float(row['price']) * int(row['quantity'])
            box_write.writerow(row)