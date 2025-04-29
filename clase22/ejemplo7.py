#Crear una funcion que va aeliminar empleados  

def verificacion(func):
    def estado(obrero):
        if obrero.get("cargo") == "administrador":
            return func(obrero)  # Pasa el objeto 'obrero' a la funcion 'eliminado'
        else:
            print( "Acceso denegado, no eres administrador no puedes eliminarlo")git status
            
    return estado
        

@verificacion
def eliminado(obrero):
    print(f"El señor {obrero['name']} ha sido eliminado")  # Accede al nombre con 'obrero["name"]'

# Creamos un administrador y un obrero
administrador = {"name": "Juan", "cargo": "administrador"}
obrero = {"name": "Paquita", "cargo": "empleado"}

# Intentamos eliminar a un obrero que no es administrador
eliminado(administrador)
eliminado(obrero)
