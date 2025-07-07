> **Elemento** que representa un **comportamiento** o **[PROCESO](/MSI/R. Pressman/PROCESO)** **dinámico** dentro de un **sistema**, modelado típicamente en un **[Diagrama de Actividad](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Actividad).**

Es una **unidad de trabajo** que describe una secuencia de **acciones** ejecutadas para alcanzar un objetivo específico, como parte de un **[Caso de Uso](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Caso de Uso)**, un proceso de negocio o una **[Interacción](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Interacción)** en el sistema.

- Representa un **proceso** que puede incluir decisiones, bucles, entradas, salidas, transiciones.
- Representa la ejecución de un cálculo. Se modela como un conjunto de nodos de actividad conectados mediante **flujos de control** (secuencia lógica de acciones con flechas) y **flujos de datos** (transferencia de datos u objetos entre acciones con flechas).
- **Actividad vs. Acción:** Una **actividad** es un proceso completo que contiene múltiples acciones. Una **acción** es un paso atómico dentro de la actividad.
- Pueden incluir **condiciones** previas y posteriores para definir **requisitos** antes o después de la actividad.
****
#### **Notación**
Un componente de una actividad son los **nodos**, que difieren de lo que definimos como **nodo** de un diagrama de despliegue. Los nodos de este inciso son elementos que representan puntos específicos en el flujo de una actividad. Incluyen:
	
- **Nodo de inicio**: Punto de partida del flujo (círculo negro).
- **Nodo de fin**: Punto de finalización (círculo con borde grueso o "X").
- **Nodo de acción**: Tarea específica (rectángulo con bordes redondeados).
- **Nodo de decisión**: Punto de bifurcación condicional (rombo).

Supongamos una actividad para "Procesar un inicio de sesión":

- **Nodo de inicio** → Acción: "Ingresar credenciales" → Nodo de decisión: "¿Credenciales válidas?"
    
	- Si sí → Acción: "Conceder acceso" → **Nodo de fin**.
    - Si no → Acción: "Mostrar error" → **Nodo de fin**.

En un **[Diagrama de Actividad](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Actividad)**, esto se representa con nodos conectados por flechas, mostrando el flujo lógico.