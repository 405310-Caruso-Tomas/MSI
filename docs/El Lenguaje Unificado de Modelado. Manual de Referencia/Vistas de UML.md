> Son una **forma de organizar y representar diferentes aspectos** de un sistema de software **mediante diagramas** del Lenguaje Unificado de Modelado ([UML](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/UML)).

Cada vista se enfoca en un conjunto específico de características o perspectivas del sistema, permitiendo a los interesados comprender y analizar el sistema desde diferentes ángulos. 
****
A continuación se adjunta una tabla con las vistas y sus correspondientes diagramas y conceptos. Para mayor entendimiento es recomendable leer el apartado de **[Áreas Conceptuales de UML](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Áreas Conceptuales de UML)**.

![Pasted image 20250622170930.png](/MSI/assets/Pasted image 20250622170930.png)
****
##### **Vista estática**

- Modela conceptos del **dominio** de la aplicación.
- Estática porque no describe el comportamiento dependiente del tiempo del sistema.
- Captura la estructura de los **objetos**. Todo lo que concierne a estructura de **datos** tradicional. Tanto los **datos**, como las **operaciones**, son cuantificadas en **clases**. Y como sabemos, los **objetos** son instancias de **clases**.
- **[Clases](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Clases)** y sus **[Relaciones](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Relaciones)** como principales componentes.
	
	- ![Pasted image 20250625101753.png](/MSI/assets/Pasted image 20250625101753.png)
- Un [Diagrama de Clases](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Clases) es donde mejor se aprecia esta vista.
****
##### **Vista de Diseño**
- Modelan la estructura de diseño de la propia aplicación, como su expansión en **clasificadores** estructurados, las **[Colaboración](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Colaboración)es** que proporcionan funcionalidad y su ensamblado a partir de **[Componente](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Componente)s** con **interfaces** bien definidas.
- Proporcionan una oportunidad para establecer una correspondencia entre las **clases** y los **componentes** de implementación.
- Refiere al **[Diagrama de Colaboración](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Colaboración)**, **[Diagrama de Estructura Interna](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Estructura Interna)**, **[Diagrama de Componentes](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Componentes)**.
****
##### **Vista de Casos de Uso**
- Modela la funcionalidad de un sistema tal como lo perciben los agentes externos, denominados actores, que interactúan con el sistema desde un punto de vista particular.
- Un caso de uso es una unidad de funcionalidad expresada como una transacción entre los actores y el sistema.
- **[Diagrama de Casos de Uso](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Casos de Uso)**.
****
##### **Vista de [Máquina de Estados](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Máquina de Estados)**
- Describe el comportamiento dinámico de los objetos, durante un periodo de tiempo, mediante el modelado de los ciclos de vida de cada clase.
****
##### **Vista de Actividad**
- Un **[Diagrama de Actividad](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Actividad)** encapsula un modelo desde la perspectiva de **[Actividad](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Actividad)**. 
- Esta vista modela los flujos de trabajo, procesos o cálculos como una secuencia de actividades conectadas por flujos de control y, en algunos casos, flujos de datos. 
- También puede mostrar la especificación de un **[Caso de Uso](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Caso de Uso)**.

**Trazando similitudes y diferencias.** Las [Máquina de Estados](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Máquina de Estados) y las **[Actividad](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Actividad)es** son similares, en tanto que ambas describen secuencias de **estados** que ocurren a lo largo del tiempo, y las condiciones que causan los cambios entre los estados. Pero se diferencian en que la primera es más reduccionista y hace enfoque en los estados de un objeto que se someten a un cómputo, mientras que la **actividad** se enfoca en los propios estados de cómputo.
****
##### **Vista de Interacción**
Describe el intercambio de secuencias de **[Mensaje](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Mensaje)s** entre las partes de un sistema. 

Bajo esta vista, el **[Diagrama de Comunicación](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Comunicación) y [Diagrama de Secuencia](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Secuencia)**. 

Los diagramas de **secuencia** muestran claramente secuencias temporales pero no muestran explícitamente relaciones entre objetos. 

Los diagramas de **comunicación** muestran relaciones entre objetos con claridad, pero las secuencias temporales se obtienen de los números de secuencia.
****
##### **Vista de Despliegue**
Vistas **arquitectónicas** que se utiliza para modelar la **estructura física** de un sistema, mostrando cómo se distribuyen los **[Componente](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Componente)s** de software en el **hardware** y **cómo interactúan** a través de la red o infraestructura física. 

Esta vista es representada principalmente mediante el **[Diagrama de Despliegue](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Despliegue)**, que describe la topología física del sistema, incluyendo **[Nodo](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Nodo)s**, **conexiones** y **[Artefacto](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Artefacto)s**. 

Muestra la disposición física de los **nodos**. También puede resaltar los **cuellos de botella en el rendimiento** debidos a la ubicación de los **artefactos** que manifiestan **componentes** independientes en diferentes **nodos**
****
##### **Vista de Gestión del Proyecto/de Agrupación**
La vista de gestión del modelo **modela** **la organización del modelo** en sí mismo.

Un modelo abarca un conjunto de **[Paquete](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Paquete)s** que contienen los elementos del modelo.

La información de la gestión del modelo se suele mostrar en un **[Diagrama de Paquetes](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Paquetes)**, que son una variedad de los **diagramas de clases**.
****
##### **Perfiles**
UML está definido utilizando un **metamodelo**, es decir, un modelo del propio lenguaje de modelado. La modificación del metamodelo es complicada, pero el mecanismo de los **[Perfil](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Perfil)es** permite cambios limitados sobre **UML** sin modificar el metamodelo subyacente. Los **perfiles** y las **[Restricción](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Restricción)es** permiten que **UML sea adaptado** a dominios o plataformas específicas.
