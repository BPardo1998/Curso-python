numbers={"Enteros":25, "Decimal": 20.4, "Fracción":2/5}
print(numbers)
print(type(numbers))

caja = numbers.keys()
print(caja)
valor = numbers.values()
print(valor)

print(type(caja))
print(type(valor))

pars = numbers.items()
print(pars)

contactos ={ "davivienda":{"Nombre": "Juan Camilo",  "Apellido": "Barrantes", "Edad": 28, "Altura": 1.80,}, "Bancolombia": {"Nombre": "Brandon Antonio",  "Apellido": "Pardo", "Edad": 26, "Altura": 1.76 }}

print(len(contactos))
empresas = contactos.keys()
print(empresas)
información = contactos.values()
print(información)

print(contactos["davivienda"])