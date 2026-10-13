"""Parte 3: peor caso, mejor caso y caso promedio de insertion sort."""

import os
import time
import matplotlib.pyplot as plt
from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]

def esta_ordenada_desc(lista) -> bool:
    """Indica si una lista esta ordenada de mayor a menor.

    Args:
        lista: lista de indices de riesgo a verificar.

    Returns:
        True si cada elemento es mayor o igual que el siguiente.
    """
    return all(lista[i] >= lista[i + 1] for i in range(len(lista) - 1))

def medir(generador, n) -> tuple[float, int]:
    datos = generador(n) 
    t0 = time.perf_counter()
    resultado, comps = insertion_sort(datos)
    t = time.perf_counter() - t0
    assert esta_ordenada_desc(resultado), "el resultado no esta ordenado"
    return t, comps


def main():
    """Corre el experimento de la Parte 3 y genera las dos graficas.

    Mide insertion sort en los tres escenarios de Tamiza para cada
    tamano de TAMANOS, imprime una tabla y guarda en graficas/ las
    figuras parte3_comparaciones.png y parte3_tiempo.png.
    """
    escenarios = {
        "A - Aleatorio (promedio)": generar_aleatorio,
        "B - Casi ordenado": generar_casi_ordenado,
        "C - Inverso (peor)": generar_inverso,
    }
    tiempos = {nombre: [] for nombre in escenarios}
    comparaciones = {nombre: [] for nombre in escenarios}

    print(f"{'n':>6} | {'escenario':<26} | {'comparaciones':>14} | {'tiempo (s)':>10}")
    for n in TAMANOS:
        for nombre, gen in escenarios.items():
            t, c = medir(gen, n)
            tiempos[nombre].append(t)
            comparaciones[nombre].append(c)
            print(f"{n:>6} | {nombre:<26} | {c:>14} | {t:>10.5f}")

    os.makedirs("graficas", exist_ok=True)

    for datos, etiqueta, archivo in [
        (comparaciones, "Numero de comparaciones", "parte3_comparaciones.png"),
        (tiempos, "Tiempo de ejecucion (s)", "parte3_tiempo.png"),
    ]:
        plt.figure(figsize=(8, 5))
        for nombre, valores in datos.items():
            plt.plot(TAMANOS, valores, marker="o", label=nombre)
        plt.xscale("log")
        plt.yscale("log")
        plt.xlabel("Tamano de entrada n")
        plt.ylabel(etiqueta)
        plt.title(f"Insertion sort: {etiqueta} vs n")
        plt.grid(True, which="both", alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join("graficas", archivo), dpi=150)
        plt.close()


if __name__ == "__main__":
    main()