# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Sebastián Berrio · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `f1dd791`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 14 / 20 |
| Calidad de la explicación teórica | 16 / 20 |
| Corrección de la implementación | 22 / 25 |
| Calidad del análisis de las gráficas | 19 / 25 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **77 / 100** |
| **Nota (0–5)** | **3.85** |

## 1. Corrección conceptual (14 / 20)
**Lo que hizo bien:**
- Dice que a n = 10 gana la fuerza bruta y que divide y vencerás gana desde n = 50, y explica el costo de las llamadas recursivas.
- En el ejemplo del máximo de un arreglo plantea `T(n) = 2T(n/2) + 1`, concluye `O(n)` y que dividir no conviene.
- Recomienda divide y vencerás, declara que es una estimación y no usa una regla de tres lineal.

**Lo que puede mejorar:**
- Dice que el subarreglo máximo dividido "queda O(n)": es `O(n log n)`, como usted mismo calculó en la pregunta 1.
- El informe no trae datos medidos que muestren el cruce en n = 50; apóyese en una tabla con los tiempos.
- En la pregunta 4 falta explicar mejor por qué combinar cuesta poco en el máximo y mucho en el subarreglo.

## 2. Calidad de la explicación teórica (16 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + n` y explica el 2, el n/2 y el costo del caso cruzado.
- Aplica el método maestro (caso 2), compara `n^(log2 2) = n` con `f(n)` y llega a `Θ(n log n)`.

**Lo que puede mejorar:**
- La explicación de por qué la fuerza bruta es `Θ(n²)` es muy corta: falta contar cuántos pares (i, j) se revisan, cerca de n²/2.

## 3. Corrección de la implementación (22 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos, no modifican la lista y `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta.
- `pruebas.py` cubre la serie de ocho días, un elemento, negativos, positivos, un caso cruzado y 25 listas aleatorias.
- Tiene type hints y docstrings en todas las funciones.

**Lo que puede mejorar:**
- Faltan líneas en blanco entre funciones y antes de la primera definición en `pruebas.py` y `medicion.py` (PEP 8).
- En el docstring de `subarreglo_maximo` se perdió la palabra "(inclusive)" en `inicio`, y la firma pedida se cambió a una sola línea.

## 4. Calidad del análisis de las gráficas (19 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas y 8 tamaños.
- Su cálculo de 4000 a 8000 coincide con la gráfica: fuerza bruta pasa de 0,7 a 2,84 s (cerca de 4 veces) y divide y vencerás de 0,01 a 0,02 s (cerca de 2 veces).

**Lo que puede mejorar:**
- No dice explícitamente si esos factores (4 y 2) coinciden con `Θ(n²)` y `Θ(n log n)`; falta esa conclusión.
- Dice que divide y vencerás "se mantiene relativamente constante": en realidad sigue creciendo, solo que mucho más despacio.

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- Carpeta en `laboratorios/lab2-divide-y-vencer/` con todos los archivos, enlaces al código y gráfica visible en el README.
- Hay varios commits con mensajes descriptivos.

**Lo que puede mejorar:**
- En las Partes 1 y 2 quedaron los textos de plantilla entre corchetes ("Cómo verificaste y qué casos cubriste...", "Nota de medición...") en lugar de su propia descripción de las pruebas y de cómo midió.
- Las instrucciones de reproducción solo sirven en Windows (`.\Activate.ps1`).

## ¿El código funciona?
Sí. Las pruebas pasan, ambas funciones coinciden con listas aleatorias y la medición corre y genera la gráfica sin errores.

## Para el próximo laboratorio
- Reemplace los textos de plantilla por su propia descripción de pruebas y mediciones.
- Después de calcular los factores al duplicar n, diga si coinciden o no con lo teórico.
- Revise que las complejidades que afirma sean coherentes con sus propias recurrencias.
- Pase PEP 8 (líneas en blanco entre funciones) antes de entregar.
