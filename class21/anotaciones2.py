from typing import Optional

def ejemplo(lista_ids : list[int], id : int)-> Optional[int]:

    if id in lista_ids:
        return id
    return None