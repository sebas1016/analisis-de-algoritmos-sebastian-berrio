def CalcularPromedio(Lista):
    s=0
    for x in Lista:
     s=s+x
    return s/len(Lista)
 
l=[1,2,3,4,5]
print(CalcularPromedio(l))

def calcular_promedio(lista: list) -> float:
    """
    Calcula el promedio de una lista de números.
    
    Args:
        lista: Una lista de número (int o float).
    
    Returns:
        El promedio de los números en la lista.
    
    """
    cantidad = 0
    for numero in lista:
     cantidad = cantidad + numero
    
    promedio = cantidad / len(lista) 
    return promedio

def main() -> None:
    """
    Función principal que ejecuta el cálculo del promedio.
    """
    l = [1, 2, 3, 4, 5]
    print(calcular_promedio(l))
    
if __name__ == "__main__":
    
    main()
