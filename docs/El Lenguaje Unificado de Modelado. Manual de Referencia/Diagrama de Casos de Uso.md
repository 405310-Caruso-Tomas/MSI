Los **casos de uso** representan todas las interacciones posibles que se describirán en los requerimientos del sistema. Los actores en el proceso **pueden ser individuos u otros sistemas** y se representan como figuras sencillas.
Cada interacción se constituye como una elipse con etiqueta. Líneas vinculan a los **[Actor](../assets/Actor.md)es** con la interacción.
![Pasted image 20250626104106.png](../assets/Pasted image 20250626104106.png.md)
Los **diagramas de casos de uso** contienen además, relaciones de dependencia, generalización y asociación, tal que los actores se conectan a los casos de uso a través de asociaciones. Los casos de uso pueden organizarse especificando **[Relaciones entre Casos de Uso](../assets/Relaciones entre Casos de Uso.md)**.
****
###### **Ejemplo de *Sommerville**
![Pasted image 20250402111914.png](../assets/Pasted image 20250402111914.png.md)
Cada **[Caso de Uso](../assets/Caso de Uso.md)** debe documentarse con una descripción textual. Ejemplo:
	*El establecimiento de consulta permite que dos o más médicos, que trabajan en* *diferentes consultorios, vean el mismo registro simultáneamente. Un médico inicia* *la consulta al elegir al individuo involucrado de un menú desplegable de médicos* *que estén en línea. Entonces el registro del paciente se despliega en sus pantallas,...*
Sin embargo, debido a que se enfocan en interacciones con el sistema, no son tan efectivas para adquirir restricciones o requerimientos empresariales y no funcionales de alto nivel, ni para descubrir requerimientos de dominio.
El UML es un estándar para modelado orientado a objetos, así que los casos de uso ahora se utilizan ampliamente para adquisición de requerimientos.
****
###### **Ejemplo de *[UML](../assets/UML.md)***
![Pasted image 20250622192850.png](../assets/Pasted image 20250622192850.png.md)
Los **[Actor](../assets/Actor.md)es** son el empleado, el supervisor y el quiosco. El quiosco es un sistema distinto que acepta peticiones de un cliente.
Los casos de uso también se pueden describir a varios niveles de detalle. Se pueden descomponer en partes y ser descritos en términos de otros casos de uso más simples. 
Un **[Caso de Uso](../assets/Caso de Uso.md)** se implementa como una **[Colaboración](../assets/Colaboración.md)** en la vista de interacción.
****
##### **[Paquete](../assets/Paquete.md) en el Diagrama de Casos de Uso**
Si el modelo de casos de uso es grande, es decir si el número de ellos es elevado es útil introducir el concepto de “**[Paquete](../assets/Paquete.md)**”.
Un **paquete** reunirá cierto número de **casos de uso** agrupados por algún criterio de homogeneidad: los que corresponden a un mismo actor, los que se refieren a un mismo proceso, etc.
![Pasted image 20250626111906.png](../assets/Pasted image 20250626111906.png.md)