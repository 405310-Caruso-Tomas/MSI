> **Objeto físico** en tiempo de ejecución que representa un **recurso computacional** que generalmente tiene por lo menos capacidad de proceso y memoria. 

Recurso **[[Clasificador]]** de cálculo de tiempo de ejecución que define una ubicación física o lógica en la que se ejecutan los elementos de software.

Es posible desplegar artefactos ejecutables en los nodos.
- Modelan los **elementos** físicos o lógicos donde el software se despliega y ejecuta, como **servidores, bases de datos o máquinas virtuales.**
- Los **nodos** pueden conectarse mediante **enlaces** (que indican comunicación o interacción entre ellos, como una **red** o un **protocolo**).
- Un nodo define una localización en la que reside un **[[Artefacto]]**.
- Se utilizan principalmente en **[[Diagrama de Despliegue]]** para modelar la arquitectura física del sistema.
- Un nodo es inherentemente parte de la vista de **implementación** y no de la vista de análisis.
Al ser un objeto físico, hay un gran número de posibilidades para sus propiedades, por lo que pueden modelarse usando [[Estereotipo]]s y [[Valores Etiquetados]].
****
##### **Notación**
Se representa como un cubo 3D (un rectángulo con perspectiva tridimensional) con el nombre del nodo dentro o encima.
Los **artefactos** o **[[Componente]]s** desplegados en el nodo se dibujan dentro del cubo o conectados a él.
Los **enlaces** entre nodos se representan como líneas sólidas, a menudo etiquetadas con el protocolo o medio de comunicación (por ejemplo, "TCP/IP").
![[Pasted image 20250623131808.png]]
Los nodos pueden ser conectados por **símbolos de asociación** a otros nodos. Una **asociación** entre dos nodos indica un camino de comunicación entre ellos. La asociación puede tener un estereotipo para indicar la naturaleza del medio de comunicación.