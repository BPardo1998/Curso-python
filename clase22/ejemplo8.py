#Decorador que comprueba que cargo tiene un empleado
def verificar_acceso(cargo_requerido):
    def decorador(func):
        def wrapper(empleado):
            if empleado.get("role") == cargo_requerido:
                return func(empleado)
            else:
                print(f"ACCESO DENEGADO, Solo el Administrador, tiene acceso para eliminar")
        return wrapper
    return decorador

def ejecutar(func):
    def wrapper(empleado):
        print(f"El empleado {empleado["name"]}, a registrado una actividad")
        return func(empleado)
    return wrapper

@verificar_acceso("admin")
@ejecutar
def eliminar_empleado(empleado):
    print(f"El empleado {empleado["name"]}, ha sido eliminado")

administrador = {"name": "Juan", "role": "admin"}
empleado = {"name": "Paquita", "role": "empleado"}

eliminar_empleado(administrador)


