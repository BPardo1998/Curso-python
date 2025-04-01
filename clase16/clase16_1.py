import json

with open('clase16/producto.json', mode = 'r')as file:
    tienda = json.load(file)

for product in tienda:
    print(f"El producto en stock es {product['name']}, el precio es: {product['price']}") 