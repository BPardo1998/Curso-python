import json

producto_original = 'clase16/producto.json'

nuevo_producto = {
    'name': 'cargador portatil',
    'price': 7500,
    'quantity': 190,
    'brand': 'Cargadores',
    'category': 'Accesortios',
    'Fecha': '09-08-2025',
}

with open(producto_original, mode='r')as file:
    tienda = json.load(file)

    tienda.append(nuevo_producto)

with open(producto_original, mode='w')as file:
    json.dump(tienda, file, indent=4)