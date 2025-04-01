import random

numero_aleatorio = random.randint(1,45)
print(numero_aleatorio)
#Hago qu eme salga yuun numero aleatorio cada vez qye renderice, para ello se utioliza.randint

colore = ['rojo', 'blanco', 'azul']
color_aleatorio =random.choice(colore)
print(color_aleatorio)

#Teniendo iun alñista de varios colores, lo que hago es que cada vez que renderizo, cada color sea variado

poker = ['rey', 'reina', 'diamantre', 'copas', '10']
random.shuffle(poker)
print(poker)

#lo que hace es desordenar la secuencia recibida, toda secuencia que este dentro de shuffle