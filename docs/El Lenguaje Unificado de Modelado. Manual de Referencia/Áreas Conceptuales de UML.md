%%Inciso incomprensible con el no entendimiento de conceptos agrupados en la carpeta "Diccionario"%%
> Son categorías definidas en la especificación de UML para clasificar diagramas según el tipo de información que modelan (estructura, comportamiento, interacción). Son parte del estándar UML y **se centran en la semántica de los diagramas.**

La **semántica**, la consideramos inherente a un [Modelo](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Modelo), y es en ese inciso donde es mencionada.
Son una guía para los modeladores sobre qué diagramas usar según el aspecto del sistema, y con qué elementos.
Los conceptos, modelos, y **elementos** de [UML](../assets/UML.md) pueden agruparse en las siguientes áreas conceptuales:
****
##### **Estructura estática** 
**[Clases](../assets/Clases.md), Atributos y Operaciones.** Esta área se centra en cómo están organizados los componentes, relaciones y propiedades de un modelo en un momento dado. 
- Los conceptos son modelados como [Clases](../assets/Clases.md).
- Varias clases pueden compartir su estructura común utilizando la generalización, herencias.
- Los objetos también tienen conexiones en tiempo de ejecución con otros objetos individuales. Estas relaciones objeto a objeto se modelan mediante **asociaciones** entre clases.
- Las clases pueden tener **interfaces**, los cuales **describen su comportamiento visible desde el exterior**. 
- Los diagramas asociados más comunes a estas áreas son el **[Diagrama de Clases](../assets/Diagrama de Clases.md), diagrama de objetos** (muestra instancias específicas de clases), **[Diagrama de Componentes](../assets/Diagrama de Componentes.md)**.
****
##### **Construcciones de Diseño**
**Clasificadores, Puertos, [Colaboración](../assets/Colaboración.md)es y [Componente](../assets/Componente.md)s.** Describe los elementos que se utilizan en la fase de diseño para modelar la arquitectura y los detalles técnicos de un sistema, orientados a la implementación.
- Un **[Clasificador](../assets/Clasificador.md) estructurado** es una extensión de una clase en UML que permite modelar su estructura interna como una colección de partes conectadas mediante conectores.
- Se suele representar en un **[Diagrama de Estructura Interna](../assets/Diagrama de Estructura Interna.md)**, donde la clase se muestra como un rectángulo que contiene partes internas (rectángulos más pequeños) unidas por líneas (conectores).

- Una clase puede encapsular su estructura interna y exponer solo ciertas interfaces al exterior mediante un **[Puerto](../assets/Puerto.md)** o más de uno.

- **[Colaboración](../assets/Colaboración.md)**, **[Diagrama de Colaboración](../assets/Diagrama de Colaboración.md)**.
****
##### **Construcciones de Despliegue**
**[Nodo](../assets/Nodo.md), [Artefacto](../assets/Artefacto.md), [Manifestación](../assets/Manifestación.md) y [Vista de Despliegue](../assets/Vista de Despliegue.md).** Son los elementos utilizados para modelar la distribución física de un sistema en ejecución, es decir, cómo los elementos de software se implementan en el hardware o infraestructura física.
- El **[Diagrama de Despliegue](../assets/Diagrama de Despliegue.md)** es el principal vehículo para la vista de despliegue, mostrando **nodos** como cubos 3D, **artefactos** como rectángulos, y **relaciones** como flechas. Además de contener la representación de todos los elementos mencionados.
****
##### **Comportamiento Dinámico**
 **[Interacción](../assets/Interacción.md),** **Vida de un Objeto**, **[Actividad](../assets/Actividad.md)**. Elementos y diagramas utilizados para modelar el comportamiento de un sistema, es decir, cómo sus componentes interactúan o cambian de estado.
 Un **[Diagrama de Casos de Uso](../assets/Diagrama de Casos de Uso.md)** **muestra cómo fluye la interacción entre usuarios y el sistema a lo largo del tiempo**, lo cual es una forma de **comportamiento observable** y no una estructura estática, por lo que se dice que pertenece a esta área conceptual.
Intentan capturar la vida de un objeto, las interacciones entre objetos y los flujos de ejecución.
- La **historia de vida de un objeto** muestra cómo este interactúa con el resto del mundo a lo largo de su existencia, enfocándose en sus estados, eventos que lo afectan, acciones que realiza y transiciones entre estados.
- Se representa mediante una **[Máquina de Estados](../assets/Máquina de Estados.md)**.
- Por ejemplo, en un sistema de biblioteca, un objeto `Libro` podría tener estados como `Disponible`, `Prestado` y `Reservado`, con transiciones desencadenadas por eventos como "prestar" o "devolver".

- Las **interacciones** se representan en un **[Diagrama de Secuencia](../assets/Diagrama de Secuencia.md)** y **[Diagrama de Comunicación](../assets/Diagrama de Comunicación.md)** (*notar diferencia entre ambos*).

- Una **actividad** representa [Flujos de Proceso](../assets/Flujos de Proceso.md), en un [Diagrama de Actividad](../assets/Diagrama de Actividad.md), que puede ser secuencial o concurrente, e incluye construcciones como **decisiones**, **bucles** y **bifurcaciones**. 
****
##### **Organización del Modelo/Elementos de Agrupación**
Refiere a cómo se estructura la información de modelado para que sea **comprensible**, **manejable** y **escalable**, especialmente en sistemas grandes.
- Los **[Paquete](../assets/Paquete.md)s** dividen un modelo grande en unidades más pequeñas y comprensibles.
- Se representan en un **[Diagrama de Paquetes](../assets/Diagrama de Paquetes.md)**. 
****
##### **Perfiles/Elementos de Anotación**
**[Perfil](../assets/Perfil.md)es, [Estereotipo](../assets/Estereotipo.md)s, [Valores Etiquetados](../assets/Valores Etiquetados.md) y [Restricción](../assets/Restricción.md)es**. Mecanismos de extensibilidad diseñados para personalizar y adaptar el lenguaje a necesidades específicas. Estas construcciones permiten a los usuarios **definir nuevos tipos de elementos**, **agregar atributos** personalizados y **establecer restricciones** adicionales, manteniendo la compatibilidad con el estándar UML.


