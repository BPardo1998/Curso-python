listado = []

def agregar_empleado(empleado):
    if empleado in listado:
        return f"Empleado {empleado} ya se encuentra agregado"
    listado.append(empleado)
    return f"Empleado {empleado} agregado correctamente"

def eliminar_empleado(empleado):
    if empleado in listado:
        listado.remove(empleado)
        return "Empleado eliminado"
    else:
        return f"No fue encoentrado el empleado {empleado} "

if __name__ =="__main__":
    print("Este es el estado del empleado")
    print(agregar_empleado("Juan"))
    print(agregar_empleado("Camila"))
    print(eliminar_empleado("Camila"))