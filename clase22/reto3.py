class Tienda:
    def __init__(self, **kwargs):
        self.productos = kwargs

    def carrito(self):
        print(f"El producto es:", self.productos)

    def calcular(self):
        total = 0
        total = sum(self.productos.values())
        print(f"El total de la compra es {total}")

    def descuento(self):
        for producto in self.productos.keys():
            if producto == "pan":
                precio_original = self.productos[producto]
                precio_descuento = precio_original * 0.5
                precio_original = precio_descuento
                print(f"{producto}, esta con descuento del 50%, su nuevo precio es {precio_descuento}")

compra = Tienda(Arros= 2700, pan= 4399, Azucae= 2343)
compra.carrito()

compra.calcular()

compra.descuento()