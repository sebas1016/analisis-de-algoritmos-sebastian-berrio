
def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insertion sort.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    a = list(datos)
    comparaciones = 0

    for j in range(1, len(a)):
        clave = a[j] 
        i = j - 1 
        while i >= 0:
            comparaciones += 1
            if a[i] < clave: 
                a[i + 1] = a[i]
                i -= 1
            else:
                break
        a[i + 1] = clave

    return a, comparaciones

def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    return _merge_sort_rec(list(datos))


def _merge_sort_rec(lista: list[int]) -> tuple[list[int], int]:
    """Aplica divide y venceras de forma recursiva sobre la lista dada.

    Divide la lista a la mitad, ordena cada mitad recursivamente y las
    combina con _merge. Una lista de 0 o 1 elementos ya esta ordenada.

    Args:
        lista: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada de mayor a menor y el numero de
        comparaciones realizadas en toda la recursion.
    """
    if len(lista) <= 1:
        return lista, 0
    mitad = len(lista) // 2
    izq, c_izq = _merge_sort_rec(lista[:mitad])
    der, c_der = _merge_sort_rec(lista[mitad:])
    res, c_mezcla = _merge(izq, der)
    return res, c_izq + c_der + c_mezcla


def _merge(izquierda: list[int], derecha: list[int]) -> tuple[list[int], int]:
    """Combina dos listas ya ordenadas en una unica lista ordenada. 
        Recorre ambas listas en paralelo, 
        comparando siempre los elementos al frente y copiando el menor, 
        hasta agotar una de las dos; despues copia lo que quede de la otra.
        
        Args: 
        izquierda: lista ordenada de menor a mayor. 
        derecha: lista ordenada de menor a mayor. 
        
        Returns: Una lista ordenada con todos los elementos de izquierda y derecha. """
    resultado: list[int] = []
    i = j = 0
    comparaciones = 0
    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1
        if izquierda[i] >= derecha[j]: 
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado, comparaciones