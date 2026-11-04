import random
from estructuras import ListaEnlazada, TablaHash

def ejecutar_pruebas():
    # --- PRUEBA 1: Búsqueda exitosa e infructuosa básica ---
    lista_simple = ListaEnlazada()
    lista_simple.insertar(1234567890, "en bodega")
    assert lista_simple.buscar(1234567890) == "en bodega"
    assert lista_simple.buscar(9999999999) is None

    tabla_simple = TablaHash(11)
    tabla_simple.insertar(1234567890, "en bodega")
    assert tabla_simple.buscar(1234567890) == "en bodega"
    assert tabla_simple.buscar(9999999999) is None

    # --- PRUEBA 2: Colisión forzada (m = 7; guías 10, 24, 17) ---
    tabla = TablaHash(7)
    guias_colision = (10, 24, 17)
    for g in guias_colision:
        assert tabla.hash(g) == 3  # Validamos que caigan en la casilla 3
        tabla.insertar(g, "en bodega")

    # Verificar que se pueden buscar todas correctamente
    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en bodega"
    assert tabla.buscar(17) == "en bodega"
    assert tabla.buscar(99) is None

    # Verificar que la lista de esa casilla tiene longitud 3 y el factor de carga es correcto
    assert tabla.casillas[3].tamano == 3
    assert tabla.factor_carga() == 3 / 7

    # --- PRUEBA 3: 20 Colecciones Aleatorias ---
    estados_posibles = ["en bodega", "en reparto", "entregado", "cancelado"]
    
    for i in range(20):
        lista_test = ListaEnlazada()
        # Usamos un tamaño de tabla cambiante para probar robustez en la dispersión
        m_aleatorio = random.randint(5, 50)
        tabla_test = TablaHash(m_aleatorio)
        
        # Insertar elementos aleatorios
        guias_insertadas = []
        cantidad_elementos = random.randint(10, 100)
        
        for _ in range(cantidad_elementos):
            # Generar una guía única de 10 dígitos aproximados
            g_aleatoria = random.randint(1000000000, 9999999999)
            if g_aleatoria not in guias_insertadas:
                est = random.choice(estados_posibles)
                lista_test.insertar(g_aleatoria, est)
                tabla_test.insertar(g_aleatoria, est)
                guias_insertadas.append(g_aleatoria)

        # Probar búsquedas exitosas (todas las guías que metimos)
        for g_existente in guias_insertadas:
            res_lista = lista_test.buscar(g_existente)
            res_tabla = tabla_test.buscar(g_existente)
            assert res_lista == res_tabla, f"Error en coincidencia para guía existente {g_existente}"

        # Probar búsquedas infructuosas (guías que no metimos)
        for _ in range(20):
            g_inexistente = random.randint(1111111111, 8888888888)
            if g_inexistente not in guias_insertadas:
                assert lista_test.buscar(g_inexistente) == tabla_test.buscar(g_inexistente)

    print("¡Todos los asserts pasaron melos! Las estructuras funcionan al pelo.")

if __name__ == "__main__":
    ejecutar_pruebas()
