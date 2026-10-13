import random

def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    ran = random.Random(semilla)
    datos = list(range(n))
    ran.shuffle(datos)
    return datos


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    ran = random.Random(semilla)
    datos = list(range(n))
    ran.shuffle(datos)
    i = int(n * 0.98)
    ordenado = datos[:i]
    
    from algoritmos import insertion_sort
    ordenado, _ = insertion_sort(ordenado)
    return ordenado + datos[i:]


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    return list(range(n))