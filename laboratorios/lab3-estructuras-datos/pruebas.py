"""
Script de pruebas unitarias y de integración para validar las estructuras.
"""

import random
from estructuras import ListaEnlazada, TablaHash


def ejecutar_pruebas() -> None:
    """Ejecuta un conjunto de pruebas automatizadas usando aserciones.

    Valida búsquedas exitosas e infructuosas, fuerza colisiones en la tabla
    hash para comprobar el encadenamiento y compara los resultados de ambas
    estructuras con 20 colecciones generadas al azar.

    Raises:
        AssertionError: Si alguna de las validaciones lógicas falla.
    """
    print("=" * 60)
    print("         INICIANDO AUDITORÍA DE ESTRUCTURAS DE DATOS         ")
    print("=" * 60)

    lista_simple = ListaEnlazada()
    lista_simple.insertar(1234567890, "en bodega")
    assert lista_simple.buscar(1234567890) == "en bodega"
    assert lista_simple.buscar(9999999999) is None

    tabla_simple = TablaHash(11)
    tabla_simple.insertar(1234567890, "en bodega")
    assert tabla_simple.buscar(1234567890) == "en bodega"
    assert tabla_simple.buscar(9999999999) is None

    tabla = TablaHash(7)
    guias_colision = (10, 24, 17)
    for g in guias_colision:
        assert tabla.hash(g) == 3
        tabla.insertar(g, "en bodega")

    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en bodega"
    assert tabla.buscar(17) == "en bodega"
    assert tabla.buscar(99) is None

    assert tabla.casillas[3].tamano == 3
    assert tabla.factor_carga() == 3 / 7

    print("\n[✔] PRUEBA DE COLISIÓN FORZADA PASADA")
    print(f" -> Guías (10, 24, 17) guardadas en casilla: {tabla.hash(10)}")
    print(f" -> Tamaño real de la lista en casilla 3: {tabla.casillas[3].tamano}")
    print(f" -> Factor de carga obtenido: {tabla.factor_carga():.4f}")
    print("-" * 60)

    estados_posibles = ["en bodega", "en reparto", "entregado", "cancelado"]
    
    print(f"{'Corrida':<10}{'Casillas (m)':<15}{'Guías (n)':<12}{'Factor Carga (alpha)':<20}")
    print("-" * 60)

    for i in range(20):
        lista_test = ListaEnlazada()
        m_aleatorio = random.randint(5, 50)
        tabla_test = TablaHash(m_aleatorio)

        guias_insertadas = []
        cantidad_elementos = random.randint(10, 100)

        for _ in range(cantidad_elementos):
            g_aleatoria = random.randint(1000000000, 9999999999)
            if g_aleatoria not in guias_insertadas:
                est = random.choice(estados_posibles)
                lista_test.insertar(g_aleatoria, est)
                tabla_test.insertar(g_aleatoria, est)
                guias_insertadas.append(g_aleatoria)

        for g_existente in guias_insertadas:
            res_lista = lista_test.buscar(g_existente)
            res_tabla = tabla_test.buscar(g_existente)
            assert res_lista == res_tabla

        for _ in range(20):
            g_inexistente = random.randint(1111111111, 8888888888)
            if g_inexistente not in guias_insertadas:
                res_lista_mal = lista_test.buscar(g_inexistente)
                res_tabla_mal = tabla_test.buscar(g_inexistente)
                assert res_lista_mal == res_tabla_mal

        alpha_actual = tabla_test.factor_carga()
        print(f"#{i+1:<9}{m_aleatorio:<15}{len(guias_insertadas):<12}{alpha_actual:.4f}")

    print("-" * 60)


if __name__ == "__main__":
    ejecutar_pruebas()
