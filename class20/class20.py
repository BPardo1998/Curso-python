
xx = 100 #Variable global

def var_local():
    x = 10  #esta seria mi variable local
    print(f"Esta es la variable local : {x}")

def var_global():
    print(f"La variable global es : {xx}")

print(xx)