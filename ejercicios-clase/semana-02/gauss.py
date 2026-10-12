def sumatoria_numeros(n: int) -> int:
    """
    Calcula la sumatoria de los números del 1 al n.

    Args:
        n (int): Número hasta el cual se desea calcular la sumatoria.

    Returns:
        int: La sumatoria de los números del 1 al n.
    """
    return n*(n+1)//2

print(sumatoria_numeros(30))  # Ejemplo de uso, debería imprimir 15