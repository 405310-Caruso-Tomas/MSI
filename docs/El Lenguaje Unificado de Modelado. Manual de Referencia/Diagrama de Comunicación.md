Un diagrama de **comunicación** está basado en el contexto proporcionado por un **[Clasificador](../assets/Clasificador.md)** estructurado. 
> Tipo de diagrama de **[Interacción](../assets/Interacción.md)** que muestra cómo los **objetos** de un sistema intercambian **[Mensaje](../assets/Mensaje.md)s** para realizar una tarea específica, destacando las **relaciones estructurales** entre ellos más que el orden temporal (a diferencia de los diagramas de secuencia).

Los roles y conectores describen la configuración de los objetos y **enlaces** que pueden ocurrir cuando se ejecuta una instancia del contexto.
**Enfoque en la estructura**:
- Muestra los **objetos** (o instancias de [Clases](../assets/Clases.md)) y los **enlaces** (relaciones o asociaciones) entre ellos.
- Los **mensajes** se representan superpuestos sobre estos enlaces, indicando cómo los objetos colaboran.
- Sólo se modelan los objetos involucrados en el contexto, aunque puede haber otros en el sistema completo.
****
##### **Notación**
Los **objetos** son representados como rectángulos con nombres en el formato `nombreObjeto:NombreClase`.
Los **enlaces** son líneas que conectan los objetos. Los **[Mensaje](../assets/Mensaje.md)s** son flechas o etiquetas sobre los enlaces, numeradas para indicar el orden de las [Interacción](../assets/Interacción.md)es (`1:autenticar(usuario, contraseña)`).
![Pasted image 20250623212322.png](../assets/Pasted image 20250623212322.png.md)