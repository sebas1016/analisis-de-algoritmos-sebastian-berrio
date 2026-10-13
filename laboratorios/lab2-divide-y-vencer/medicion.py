import random
import time
from pathlib import Path
import matplotlib.pyplot as plt
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

TAMANOS = [10, 50, 100, 500, 1000, 2000, 4000, 8000]
SEMILLA = 42
REPETICIONES = 3
CARPETA_GRAFICAS = Path("graficas")

def generar_datos(n: int, generador: random.Random) -> list[int]:
    """Genera una serie de variaciones diarias de caja.

        Args:
            n: cantidad de dias de la serie.
            generador: generador aleatorio con la semilla ya fijada.

        Returns:
            Lista de n enteros entre -100 y 100.
    """
    return [generador.randint(-100, 100) for _ in range(n)]


def medir_fuerza_bruta(valores: list[int]) -> tuple[float, float]:
    """Cronometra la fuerza bruta sobre una serie.

        Args:
            valores: variacion diaria de caja.

        Returns:
            Una tupla (segundos, suma) con el menor tiempo de las repeticiones
            y la suma maxima encontrada.
    """
    mejor_tiempo = float("inf")
    suma = 0.0
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        resultado = subarreglo_fuerza_bruta(valores)
        tiempo = time.perf_counter() - inicio
        suma = resultado[2]
        if tiempo < mejor_tiempo:
            mejor_tiempo = tiempo
    return mejor_tiempo, suma


def medir_divide_y_venceras(valores: list[int]) -> tuple[float, float]:
    """Cronometra el divide y venceras sobre una serie.

        Args:
            valores: variacion diaria de caja.

        Returns:
            Una tupla (segundos, suma) con el menor tiempo de las repeticiones
            y la suma maxima encontrada.
    """
    mejor_tiempo = float("inf")
    suma = 0.0
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        resultado = subarreglo_maximo(valores, 0, len(valores) - 1)
        tiempo = time.perf_counter() - inicio
        suma = resultado[2]
        if tiempo < mejor_tiempo:
            mejor_tiempo = tiempo
    return mejor_tiempo, suma


def ejecutar_experimento() -> tuple[list[float], list[float]]:
    """Mide ambos algoritmos en cada tamano y verifica que coincidan.

        Returns:
            Una tupla (tiempos_fuerza_bruta, tiempos_divide_y_venceras) en
            segundos, en el mismo orden que TAMANOS.
    """
    generador = random.Random(SEMILLA)
    tiempos_fb: list[float] = []
    tiempos_dv: list[float] = []
    print(f"{'n':>6} {'fuerza bruta (s)':>18} {'divide y venceras (s)':>22}")
    for n in TAMANOS:
        valores = generar_datos(n, generador)
        tiempo_fb, suma_fb = medir_fuerza_bruta(valores)
        tiempo_dv, suma_dv = medir_divide_y_venceras(valores)
        assert suma_fb == suma_dv, f"Las sumas difieren para n={n}"
        tiempos_fb.append(tiempo_fb)
        tiempos_dv.append(tiempo_dv)
        print(f"{n:>6} {tiempo_fb:>18.6f} {tiempo_dv:>22.6f}")
    return tiempos_fb, tiempos_dv


def graficar(
    tiempos_fb: list[float],
    tiempos_dv: list[float],
    nombre: str
) -> None:
    """Dibuja tiempo vs tamano de entrada y guarda la imagen.

        Args:
            tiempos_fb: tiempos de la fuerza bruta, en segundos.
            tiempos_dv: tiempos del divide y venceras, en segundos.
            nombre: nombre del archivo PNG dentro de la carpeta de graficas.
    """
    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    plt.figure(figsize=(8, 5))
    plt.plot(TAMANOS, tiempos_fb, marker="o", label="Fuerza bruta")
    plt.plot(TAMANOS, tiempos_dv, marker="s", label="Divide y venceras")
    plt.title("Tiempo de ejecucion vs tamano de entrada")
    plt.xlabel("Tamano de entrada n (numero de dias)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / nombre, dpi=150)
    plt.close()


def main() -> None:
    """Ejecuta el experimento y genera las graficas."""
    tiempos_fb, tiempos_dv = ejecutar_experimento()
    graficar(tiempos_fb, tiempos_dv, "tiempo_vs_n.png")
   

if __name__ == "__main__":
    main()