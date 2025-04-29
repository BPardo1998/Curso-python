from collections import Counter
#Counter es una herramienta que al utilizarla, me muestra cuantas veces esta un producto en una lista de productos
def ventas(productos: list[str]) -> Counter:
    return Counter(productos)

sales = ['papel', 'computador', 'papel', 'esfero']
resultado = ventas(sales)
print(resultado)