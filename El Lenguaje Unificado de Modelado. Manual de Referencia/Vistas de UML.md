> Son una forma de organizar y representar diferentes aspectos de un sistema de software mediante diagramas del Lenguaje Unificado de Modelado ([[UML]]).

Cada vista se enfoca en un conjunto específico de características o perspectivas del sistema, permitiendo a los interesados comprender y analizar el sistema desde diferentes ángulos.
****
A continuación se adjunta una tabla con las vistas y sus correspondientes diagramas y conceptos. Para mayor entendimiento es recomendable leer el apartado de **[[Áreas Conceptuales de UML]]**.
![[Pasted image 20250622170930.png]]
****
##### **Vista estática**
- Modela conceptos del dominio de la aplicación.
- Estática porque no describe el comportamiento dependiente del tiempo del sistema.
- Clases y sus [[Relaciones]] como principales componentes.
- Un [[Diagrama de Clases]] es donde mejor se aprecia esta vista.
****
##### **Vista de Diseño**
- Modelan la estructura de diseño de la propia aplicación, como su expansión en clasificadores estructurados, las colaboraciones que proporcionan funcionalidad y su ensamblado a partir de componentes con interfaces bien definidas.
- Proporcionan una oportunidad para establecer una correspondencia entre las clases y los componentes de implementación.
- Refiere al **[[Diagrama de Colaboración]]**, **[[Diagrama de Estructura Interna]]**, **[[Diagrama de Componentes]]**.
****
##### **Vista de Casos de Uso**
- Modela la funcionalidad de un sistema tal como lo perciben los agentes externos, denominados actores, que interactúan con el sistema desde un punto de vista particular.
- Un caso de uso es una unidad de funcionalidad expresada como una transacción entre los actores y el sistema.
- **[[Diagrama de Casos de Uso]]**.
****
##### **Vista de [[Máquina de Estados]]**
****
##### **Vista de Actividad**
- Un **[[Diagrama de Actividad]]** encapsula un modelo desde la perspectiva de actividad. 
- Esta vista modela los flujos de trabajo, procesos o cálculos como una secuencia de actividades conectadas por flujos de control y, en algunos casos, flujos de datos. 
- También puede mostrar la especificación de un caso de uso.
****
##### **Vista de Interacción**
Describe el intercambio de secuencias de mensajes entre las partes de un sistema. 
Una interacción está basada en un clasificador estructurado o en una colaboración.
Un rol es una ranura que debe ser rellenada con objetos en un uso concreto de una interacción.
Esta vista proporciona una visión integral del comportamiento de un sistema, es decir, muestra el flujo de control a través de varios objetos. La vista de interacción se muestra mediante dos diagramas que se centran en aspectos distintos: **[[Diagrama de Secuencia]]** y **[[Diagrama de Comunicación]]**. 

Una máquina de estados, como vimos, es una vista reduccionista que mira a cada objeto individualmente. Sin embargo, puede ser difícil comprender el funcionamiento completo de un sistema porque una máquina de estados se centra en un solo objeto en cada momento. La vista de interacción proporciona una vista más integral del comportamiento de un conjunto de objetos. Esta vista se modela median te interacciones que actúan sobre clasificadores estructurados y colaboraciones.
