# Plataforma Tamiza: análisis de algoritmos

## Introducción

La Secretaría de Salud utiliza la plataforma Tamiza para organizar los resultados de tamizaje cardiovascular de 340 laboratorios e IPS. Actualmente hay **1.200.000 registros pendientes de gestión** y el sistema debe ordenarlos por índice de riesgo, de mayor a menor, entre las 2:00 a. m. y las 6:00 a. m.

El algoritmo que se utiliza es **insertion sort**. Aunque antes funcionaba con una cantidad menor de registros, ahora no siempre termina dentro del tiempo disponible. A continuación, se analiza por qué es necesario revisar el algoritmo y qué responsabilidades ambientales y éticas implica esta decisión.

## Parte 1. Análisis del algoritmo antes de comprar hardware
Considero que se debe analizar primero el algoritmo porque el hecho de que haya funcionado durante ocho años no significa que siendo idóneo para la cantidad de datos que procesar en la actualidad.

Se debe diferenciar entre la corrección y la eficiencia con respecto al tiempo de ejecución. La corrección es la que se encarga del ordenamiento de los registros filtrando por el indice de riesgo, del mas alto al mas bajo. Por otro lado, la eficiencia con respecto al tiempo que consiste en realizar ese trabajo dentro del plazo disponible. Un algoritmo puede entregar una lista correctamente ordenada, pero tardar tanto que el resultado no este listo o disponible cuando se necesite.

La restricción que se incumple es la ventana de cuatro horas. (Entre las 2:00 AM y las 6:00AM) El algoritmo actual, Insertion sort, se conoce por su crecimiento cuadrático donde el peor caso es O(n²), lo que nos indica que al aumentar la cantidad de datos o registros el trabajo o procesamiento que se debe hacer aumenta mucho más que la cantidad de datos a procesar.

Exactamente por esa misma razón, duplicar el la velocidad del servidor no es una solución viable, porque al tener una computadora más rápida podría servir muy superficialmente, si hablamos que duplicamos su velocidad, estamos diciendo que la mejoramos por dos, mientras que los datos crecen de forma cuadrática, es cuestión de tiempo para que vuelva y falle. El problema no es necesariamente la maquina, si no el algoritmo que se usa para el procesamiento de datos. Por eso primero evaluaría un algoritmo como merge sort, cuyo tiempo de ejecución crece como O(n log(n)), y se compara con los tres escenarios, así dar el dictamen correcto si hace falta mejorar el hardware o no.

Un ejemplo diferente sería. Un sistema de gestión de inventario de una bodega o negocio que debe ordenar alrededor de 200,000 registros de salida, para generar una alerta diaria antes de cerrar la bodega entre las 4:00 PM y las 6:00 PM para así tener un reporte diario y poder surtir, p se utiliza insertion sort va requerir una cantidad muy grande de procesamiento, y no alcanzar la ventana de 2 horas. Puede que termine después pero no va alcanzar para surtir.

En conclusión, antes de invertir en una mejor maquina o servidor mas potente, se debe analizar el algoritmo para poder dar el dictamen correcto.

## Parte 2. Responsabilidad ambiental y ética de la implementación

Como responsable técnico de Tamiza, considero que elegir un algoritmo no consiste solamente en conseguir que el programa funcione, si no también en pensar en sus consecuencias ambientales y para las personas que dependen de sus resultados.

### Dimensión ambiental.

El tiempo que tarda el algoritmo en ordenar los 1.200.000 registros, se va consumir mas energía durante el procesamiento nocturno. Mientras el programa se ejecuta, el servidor va estar funcionando a una muy alta capacidad, ademas si le sumamos el tiempo de operación, el consumo de energía se va subir mucho, y por ende el impacto ambiental va a ser mas significativo.

Esto también se debe analizar a largo plazo. Tamiza ejecuta este proceso todas las madrugadas entre las 2:00 Am y 6:00 Am, así que aunque sean 4 horas en un día, el acumulado durante meses o años, va a ser una diferencia muy significativa. Si se mantiene un algoritmo que necesita demasiado tiempo, se podria gastar energía innecesariamente. Además, comprar un servidor del doble de velocidad también va a consumir energía indirectamente y dejar incluso un impacto ambiental más marcado, por todo el proceso de fabricación y mantener otro equipo.

Por eso considero que se debe buscar un algoritmo que ordene los registros en menos tiempo y medir el consumo real antes y después del cambio. Así se puede reducir el uso innecesario  de energía sin afectar el resultado.

### Dimensión ética

La demora o el fallo del algoritmo puede perjudicar directamente a los pacientes.

 **Un paciente con riesgo cardiovascular alto queda de la lista del día.** 
 Si el proceso no termina en el tiempo requerido, este paciente podría no recibir una llamada para solicitar sus valoración médica. Si necesita atención prioritaria, el retraso puede afectar su salud. En este caso, el paciente asume el mayor costo, porque soporta las posibles consecuencias del retraso. La secretaría también tiene responsabilidad por garantizar el correcto procesamiento.

**Un paciente con riesgo bajo aparece antes que otro con riesgo alto.** Si la lista queda a medias o se genera incorrectamente, el operador. Puede suceder que se llame primero a un paciente que necesite menos prioridad,  mientras que otra persona que requiere atención más urgente debe esperar. El operador asume el costo operativo de trabajar con una lista defectuosa, pero no debería ser responsabilizado por un fallo técnico que no puede controlar. El equipo de desarrollo y la Secretaria deben responder por la calidad del sistema y sus controles.

### La prioridad de las llamadas también es una responsabilidad ética

El ordenamiento no es una operación sencilla sin responsabilidad, es la que determina quien recibe primero la prioridad al ser contactado. Por eso, no basta con que el algoritmo termine dentro de las cuatro horas. También debe ordenar correctamente los índices de riesgo, sin perder registros no modificar sus valores.

Además se deben verificar los resultados, conservar una trazabilidad de los registros, hacer un seguimiento y establecer un criterio para pacientes con el mismo indice de riesgo. Estas medias ayudan a evitar decisiones arbitrarias y permiten detectar errores.

En conclusión, considero que la responsabilidad técnica consiste en buscar un algoritmo que cumpla con el tiempo establecido, reduzca el consumo innecesario de recursos y respete la prioridad médica de los pacientes. Una decisión técnica incorrecta puede terminar afectando a personas que dependen de este servicio.
## Conclusión general.
El caso de Tamiza muestra que un algoritmo puede producir resultados correctos y, aun así, no servir para las necesidades actuales si no termina a tiempo. Antes de comprar hardware, siempre es importante comparar alternativas de ordenamiento y probarlas con los diferentes tipos de entrada. La decisión también debe considerar el consumo energético acumulado en el tiempo y las consecuencias para los pacientes.
