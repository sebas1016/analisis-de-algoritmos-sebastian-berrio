import random

from subarreglo import suma_cruzada, subarreglo_fuerza_bruta, subarreglo_maximo

def resolver_ambos(serie: list[float]) -> tuple[float, float]:
    """Resuelve una serie con ambos algoritmos y valida sus resultados.

        Ejecuta la fuerza bruta y el divide y venceras sobre la misma serie,
        comprueba que la lista original no se modifique y que la suma de cada
        tramo devuelto coincida con la suma reportada.

        Args:
            serie: variacion diaria de caja, con al menos un elemento.

        Returns:
            Una tupla (suma_fuerza_bruta, suma_divide_y_venceras) con la suma
            maxima encontrada por cada algoritmo.
    """
    copia = list(serie)
    fb_i, fb_j, fb_suma = subarreglo_fuerza_bruta(serie)
    dv_i, dv_j, dv_suma = subarreglo_maximo(serie, 0, len(serie) - 1)
    assert serie == copia  # ninguna funcion modifica la lista
    assert sum(serie[fb_i:fb_j + 1]) == fb_suma
    assert sum(serie[dv_i:dv_j + 1]) == dv_suma
    return fb_suma, dv_suma

serie = [-3, 5, -2, 8, -6, 3, 9, -4]

assert subarreglo_fuerza_bruta(serie)[2] == 17
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17
assert resolver_ambos([7]) == (7, 7)
assert resolver_ambos([-7]) == (-7, -7)
assert resolver_ambos([-8, -3, -6, -2, -9]) == (-2, -2)
assert resolver_ambos([4, 1, 7, 3]) == (15, 15)

cruzado = [-5, 4, 3, -1, 6, -7]
assert resolver_ambos(cruzado) == (12, 12)
assert suma_cruzada(cruzado, 0, 2, 5) == (1, 4, 12)

for _ in range(25):
    n = random.randint(1, 60)
    aleatoria = [random.randint(-20, 20) for _ in range(n)]
    fb_suma, dv_suma = resolver_ambos(aleatoria)
    assert fb_suma == dv_suma

print("Todas las pruebas pasaron")