ejemplo = 10

def modificación():
    global ejemplo
    ejemplo += 5
    print(f"El valor modificado es : {ejemplo}")

modificación()
print(ejemplo)