"""
Script para medir tiempos de ejecución y generar gráficas del laboratorio.
"""

import os
import random
import time
import matplotlib.pyplot as plt
from estructuras import ListaEnlazada, TablaHash


def generar_guias_inexistentes(existentes: set[int], cantidad: int, semilla: int = 7) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def es_primo(num: int) -> bool:
    """Verifica si un numero entero es primo.

    Args:
        num: El numero a evaluar.

    Returns:
        True si es primo, False de lo contrario.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def buscar_primo_cercano(objetivo: int) -> int:
    """Encuentra el numero primo mas cercano a un valor objetivo.

    Args:
        objetivo: El valor al que queremos aproximarnos.

    Returns:
        El primer numero primo igual o mayor al objetivo.
    """
    candidato = max(2, objetivo)
    while not es_primo(candidato):
        candidato += 1
    return candidato


def experimento_a() -> None:
    """Ejecuta el experimento A comparing la lista y la tabla hash.

    Mide el tiempo promedio de busqueda infructuosa con diferentes tamaños
    de datos (n) y guarda la grafica correspondiente.
    """
    valores_n = [100, 500, 1000, 5000, 10000, 20000]
    tiempos_lista = []
    tiempos_tabla = []

    # Semilla fija para crear datos iniciales
    azar_datos = random.Random(42)
    estados_posibles = ["en bodega", "en reparto", "entregado"]

    for n in valores_n:
        lista = ListaEnlazada()
        m_primo = buscar_primo_cercano(n // 2)
        tabla = TablaHash(m_primo)

        existentes_set = set()
        guias_locales = []

        while len(existentes_set) < n:
            g = azar_datos.randint(10**9, 10**10 - 1)
            if g not in existentes_set:
                existentes_set.add(g)
                guias_locales.append(g)

        for g in guias_locales:
            est = azar_datos.choice(estados_posibles)
            lista.insertar(g, est)
            tabla.insertar(g, est)

        for g_muestra in guias_locales[:10]:
            assert lista.buscar(g_muestra) == tabla.buscar(g_muestra)

        malas = generar_guias_inexistentes(existentes_set, 200, semilla=7)

        inicio_l = time.perf_counter()
        for mala in malas:
            lista.buscar(mala)
        fin_l = time.perf_counter()
        tiempos_lista.append((fin_l - inicio_l) / 200)

        inicio_t = time.perf_counter()
        for mala in malas:
            tabla.buscar(mala)
        fin_t = time.perf_counter()
        tiempos_tabla.append((fin_t - inicio_t) / 200)

    # Crear la gráfica
    plt.figure(figsize=(8, 5))
    plt.plot(valores_n, tiempos_lista, "o-", label="Lista Enlazada", color="red")
    plt.plot(valores_n, tiempos_tabla, "s-", label="Tabla Hash (α ≈ 2)", color="blue")
    plt.title("Búsqueda Inexistente: Lista Enlazada vs Tabla Hash")
    plt.xlabel("Cantidad de Guías Guardadas (n)")
    plt.ylabel("Tiempo Promedio por Búsqueda (segundos)")
    plt.grid(True)
    plt.legend()
    
    os.makedirs("graficas", exist_ok=True)
    plt.savefig("graficas/lista_vs_tabla.png")
    plt.close()


def experimento_b() -> None:
    """Ejecuta el experimento B analizando el efecto del factor de carga.

    Mantiene n fijo en 20000 y varia m para alterar alfa, midiendo
    el impacto en el tiempo de busqueda fallida.
    """
    n_fijo = 20000
    alfas = [0.5, 1.0, 4.0, 10.0]
    tiempos_alfa = []

    azar_datos = random.Random(99)
    estados_posibles = ["en bodega", "en reparto", "entregado"]

    existentes_set = set()
    guias_locales = []
    while len(existentes_set) < n_fijo:
        g = azar_datos.randint(10**9, 10**10 - 1)
        if g not in existentes_set:
            existentes_set.add(g)
            guias_locales.append(g)

    malas = generar_guias_inexistentes(existentes_set, 200, semilla=7)

    for alfa in alfas:
        m_calculado = int(n_fijo / alfa)
        # Aseguramos que m sea al menos 1
        m_calculado = max(1, m_calculado)
        
        tabla = TablaHash(m_calculado)

        for g in guias_locales:
            est = azar_datos.choice(estados_posibles)
            tabla.insertar(g, est)

        inicio = time.perf_counter()
        for mala in malas:
            tabla.buscar(mala)
        fin = time.perf_counter()
        tiempos_alfa.append((fin - inicio) / 200)

    # Crear la gráfica
    plt.figure(figsize=(8, 5))
    plt.plot(alfas, tiempos_alfa, "d-", color="purple", label="Tabla Hash")
    plt.title("Efecto del Factor de Carga (alfa) en la Tabla Hash")
    plt.xlabel("Factor de Carga (alfa = n / m)")
    plt.ylabel("Tiempo Promedio por Búsqueda (segundos)")
    plt.grid(True)
    plt.legend()
    
    os.makedirs("graficas", exist_ok=True)
    plt.savefig("graficas/tiempo_vs_alfa.png")
    plt.close()


if __name__ == "__main__":
    experimento_a()
    experimento_b()
    print("¡Listo! Las dos gráficas se crearon en la carpeta 'graficas/'.")
