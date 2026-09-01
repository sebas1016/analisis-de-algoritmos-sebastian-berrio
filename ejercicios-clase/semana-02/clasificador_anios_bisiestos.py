"""Clasificador de años bisiestos.
 
Complete las funciones siguiendo la especificación de cada docstring.
"""

def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
 
    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.
 
    Args:
        anio: año a evaluar (número entero).
 
    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def leer_anios() -> list:
    """
    Solicita al usuario una lista de años separados por comas.
 
    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).
 
    Returns:
        Lista de años como enteros.
    """
    try:
        anios_str = input("Ingrese una lista de años separados por comas: ")
        anios = [int(anio.strip()) for anio in anios_str.split(",")]
        return anios
    except ValueError:
        print("Error: Por favor, ingrese solo números enteros separados por comas.")
        return []

def main() -> None:
    """
    Punto de entrada del Script.
    """
    anios = leer_anios()
    anio_bisiesto = [anio for anio in anios if es_bisiesto(anio)]
    print(f"Hay {len(anio_bisiesto)} años bisiestos en la lista ingresada: {anio_bisiesto}")

if __name__ == "__main__":
    main()