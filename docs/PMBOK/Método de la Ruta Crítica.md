Se utiliza para estimar la duración mínima del proyecto y determinar el nivel de flexibilidad en la programación de los caminos de red lógicos dentro del cronograma.

Relevante para la [Gestión del Tiempo del Proyecto](/MSI/PMBOK/Gestión del Tiempo del Proyecto).
****
Esta técnica de análisis de la red del cronograma calcula las fechas de inicio y finalización, tempranas y tardías, para todas las actividades, sin tener en cuenta las limitaciones de recursos, y realiza un análisis que recorre hacia adelante y hacia atrás toda la red del cronograma como muestra la imagen.
Cada letra corresponde a una actividad, se comienza en A, y B y C dependen de A.

![Pasted image 20250613115547.png](/MSI/assets/Pasted image 20250613115547.png)

Lo que se hace principalmente es definir la **Ruta Crítica**, es decir, la secuencia más larga de actividades en el proyecto que no puede retrasarse sin afectar la fecha de finalización del proyecto. Las actividades en esta ruta tienen holgura (float) igual a cero, lo que significa que no hay margen para retrasos.
En este ejemplo el camino más largo incluye las actividades A, C y D, y por lo tanto la secuencia A-C-D constituye la ruta crítica.
****
**Resultados**:

- Duración total del proyecto.
- Actividades críticas que requieren especial atención.
- Identificación de actividades con holgura, lo que permite optimizar recursos o ajustar el cronograma.
****
###### **Esclarecimiento**
En el ejemplo, la ruta crítica es A-C-D, pero esto no significa que B no deba realizarse, o que no forme parte del proyecto, simplemente significa que B tiene holgura, lo que permite cierta flexibilidad en su ejecución sin afectar la duración total del proyecto.

Puede ejecutarse, primero A por supuesto, y luego B y C en simultáneo, pero priorizar A y C es crucial porque al ser la ruta crítica, cualquier retraso en ellas extenderá la duración del proyecto, y la realización de D.