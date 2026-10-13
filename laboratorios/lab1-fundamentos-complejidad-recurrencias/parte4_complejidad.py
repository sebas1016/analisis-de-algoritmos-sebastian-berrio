import math
import os
import time
import matplotlib.pyplot as plt
from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3  
N_PRODUCCION = 1_200_000
VENTANA_S = 4 * 3600


def medir(algoritmo, datos) -> tuple[float, int]:
    """Mide el tiempo de un algoritmo de ordenamiento sobre una entrada.

    Repite la medicion REPETICIONES veces y conserva el menor tiempo para
    reducir el ruido del sistema. Solo se cronometra el algoritmo.

    Args:
        algoritmo: funcion que recibe la lista y devuelve (lista, comparaciones).
        datos: lote de registros a ordenar.

    Returns:
        Una tupla (mejor tiempo en segundos, numero de comparaciones).
    """
    mejor = float("inf")
    for _ in range(REPETICIONES):
        t0 = time.perf_counter()
        _, comps = algoritmo(datos)       # solo se cronometra el algoritmo
        mejor = min(mejor, time.perf_counter() - t0)
    return mejor, comps


def main():
    """Compara insertion sort y merge sort sobre el escenario A.

    Imprime una tabla de tiempos y comparaciones, guarda la grafica
    graficas/parte4_tiempo.png y calcula la extrapolacion a 1.200.000
    registros (estimacion, no medicion) para el concepto tecnico.
    """
    t_ins, t_mer = [], []
    print(f"{'n':>6} | {'insertion (s)':>14} | {'merge (s)':>10} | {'comps ins':>12} | {'comps merge':>12}")
    for n in TAMANOS:
        datos = generar_aleatorio(n)
        ti, ci = medir(insertion_sort, datos)
        tm, cm = medir(merge_sort, datos)
        t_ins.append(ti)
        t_mer.append(tm)
        print(f"{n:>6} | {ti:>14.5f} | {tm:>10.5f} | {ci:>12} | {cm:>12}")

    os.makedirs("graficas", exist_ok=True)
    plt.figure(figsize=(8, 5))
    plt.plot(TAMANOS, t_ins, marker="o", label="Insertion sort")
    plt.plot(TAMANOS, t_mer, marker="s", label="Merge sort")
    plt.xlabel("Tamano de entrada n (numero de registros)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.title("Insertion sort vs merge sort - escenario A (aleatorio)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join("graficas", "parte4_tiempo.png"), dpi=150)
    plt.close()

    # Extrapolacion (ESTIMACION, no medicion) para 4.3
    n = TAMANOS[-1]
    k_ins = t_ins[-1] / n ** 2
    k_mer = t_mer[-1] / (n * math.log2(n))
    est_ins = k_ins * N_PRODUCCION ** 2
    est_mer = k_mer * N_PRODUCCION * math.log2(N_PRODUCCION)
    print(f"\nEstimacion para n = {N_PRODUCCION:,} (escenario A):")
    print(f"  insertion sort: {est_ins / 3600:.1f} horas (ventana: 4 h)")
    print(f"  merge sort:     {est_mer / 60:.1f} minutos")
    print(f"  razon de tiempos a n={n}: {t_ins[-1] / t_mer[-1]:.0f}x")


if __name__ == "__main__":
    main()