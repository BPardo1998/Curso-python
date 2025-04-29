from enum import Enum

class EstadoOrden(Enum):
    Pendiente = 1
    emviado = 2
    Entregado = 3

def verificarEstado(estado : EstadoOrden):
    if estado == EstadoOrden.Pendiente:
        return "Se encuentra en estado de pendiente"
    elif estado == EstadoOrden.emviado:
        return "Se encuentra en tramite"
    elif estado == EstadoOrden.Entregado:
        return "El paquerte fue entregado"

print(verificarEstado(EstadoOrden.emviado))