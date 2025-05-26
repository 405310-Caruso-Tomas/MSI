 ***Modelo***. Arquetipo o punto de referencia. Representación simplificada de un objeto, sistema, proceso o idea que se utiliza para comprender cómo funciona.
**REPRESENTACIÓN DE UN OBJETO, SISTEMA O IDEA**, de forma diferente al de la entidad misma. 

> En la actualidad son muchos los esfuerzos que se realizan por solucionar los inconvenientes que se producen en el proceso de captura de requerimientos funcionales en la creación de un Modelo Conceptual, esto queda evidenciado por la gran cantidad de metodologías y herramientas existentes.
*****
###### **Modelar**
El propósito de los modelos es ayudarnos a explicar, entender y mejorar dicha entidad. Al modelar, se busca atacar a un problema difícil dividiéndolo en una serie de problemas más pequeños que se puedan resolver.

Un Modelo deberá representar fiel y completamente los [[Requerimientos]] de los usuarios. Además de describir al sistema con suficiente detalle como para hacer predicciones válidas sobre el comportamiento de este.
****
***Desde la óptica disciplinar de los Sistemas de Información y los Sistemas de Software*** asociados a ellos, un **Esquema Conceptual** será definido como un Modelo de representación de la realidad sobre un dominio de problema determinado, pero a diferencia del Modelo (donde se busca solamente comunicar el dominio del problema), el esquema incluye detalles de implementación, estructura, cardinalidad, atributos específicos.

> Las debilidades de la mayoría de los métodos para la obtención de esquemas conceptuales se reflejan en las primeras etapas del desarrollo de software, lo que trae aparejado un costo **excesivamente** alto en tareas de reproceso. El principal problema derivado de estas debilidades radica en la imposibilidad de determinar si el modelo conceptual construido, refleja completamente la esencia del dominio que se intenta representar.

En el desarrollo de software se aplican distintos tipos de **Patrones** (soluciones generalizadas) y entre los más renombrados encontramos los Patrones de Diseño y los Patrones Arquitectónicos. 
Pero también existe un grupo de Patrones menos conocidos los cuales pueden ser utilizados en etapas tempranas, previas a la fase de Desarrollo, y se conocen como **Patrones*** **de** **Negocio**.

La tendencia actual es lo que se denomina Desarrollo de Software Dirigido por Modelos (DSDM), o también MDD (Model Driven software Development). [[Desarrollo Dirigido por Modelos]]
****
###### **Clasificación**
Existen modelos esquemáticos que abarcan dibujos, mapas y diagramas. Existen modelos simbólicos, los cuales están basados en las matemáticas o en un código de computadora. Incluso modelos físicos tales como el modelo de un avión.
Una forma de clasificarlos es según la forma que representan el **tiempo**:

**ESTÁTICOS**: Un modelo estático omite ya sea un reconocimiento del tiempo o describe un instante del estado de un sistema en determinado momento. Debe proporcionar, y especificar propiedades no cambiantes, de manera que se soporte toda la funcionalidad requerida del Modelo.

**DINÁMICOS**: Un modelo dinámico reconoce explícitamente el transcurso del tiempo. Proporciona una secuencia de estados del sistema en el tiempo. Ciclo de vida de los objetos e interrelaciones que se producen entre los mismos.
****
###### **Necesidad y costo del nivel de detalle**
Un modelo es una abstracción. **Cuanto más detallado el modelo, mejor se asemejará a la realidad.** Se conoce más sobre el comportamiento del sistema de esta forma.

Por otra parte, **mucho detalle dificulta la comprensión** de las soluciones propuestas a los requerimientos a satisfacer.

Sin embargo, el factor que sirve de límite en la utilización del detalle, es que a menudo no se tiene suficiente información sobre los propósitos del dominio. De todas formas, todo modelo debe limitar el detalle en algún aspecto.
****
> Cuanta mayor envergadura tenga el sistema a construir, hay más probabilidades que se fracase si no se construye el modelo adecuado. Todos los sistemas útiles e interesantes tienen la tendencia natural de hacerse más complejos con el paso del tiempo.
###### **Principios del Modelado**
En las disciplinas ingenieriles el uso del modelado tiene una larga y rica experiencia, la que sugiere cuatro principios básicos:
	• La **elección del Modelo** que se utilizará tendrá una **incidencia directa** en la forma que tomará la solución.
	• Todo Modelo puede ser obtenido con diferentes grados de precisión (nivel de **granularidad**). 
	• Todo Modelo **debe reflejar las características esenciales de la realidad** (Requisitos Funcionales).
	• **Un único Modelo no es suficiente**. Resulta más ventajoso disponer de un conjunto de diferentes perspectivas.
****
###### **Uso de Metodologías en el modelado**
En el modelado, especialmente en el contexto de los sistemas de información, se emplean diversas metodologías que buscan estructurar, representar y analizar la información de manera sistemática. [[Metodologías de Modelado]].
****
###### **Características deseables de las metodologías y herramientas**
- **Modelado iterativo y evolutivo**: Las actividades de elicitación, especificación y validación deberían ser repetidas varias veces en un proceso iterativo, de forma que los requerimientos sean refinados y evolucionen, como es detallado en el apartado de [[Ingeniería de Requerimientos]]. 
	- En cada iteración el Modelo debe permitir identificar el origen del requerimiento, y el versionado actual de los mismos. De forma que figure como un seguimiento durante todo el proceso de modelado, hasta su efectivo cumplimiento plasmado en la funcionalidad del Modelo.

- **Diferentes vistas**: vistas que son importantes que estén presentes en cualquier conjunto de metodologías para facilitar la comprensión del sistema: vista *estática, dinámica y funcional* (especifica en forma declarativa, cómo en cada servicio, ante un estímulo, se producen los cambios de estados en sus atributos.)

- **Documentación proporcionada por el Modelo**: La misma debe estar destinada al cliente de manera que certifique los requisitos a satisfacer, y que a su vez, sirva como insumo en las restantes etapas de construcción del sistema.

- **Flexibilidad para cambio de Requisitos**: El Modelo debe ser flexible, permitiendo introducir cambios. Y a su vez, se debe realizar una evaluación de impacto que producirá en el resto del sistema la modificación introducida.

- **Notación favorable**: El lenguaje natural es inherentemente ambiguo, por lo tanto, se deberá procurar llevar a una notación que permita reducir la ambigüedad y unificar el léxico empleado por el usuario, en lo posible.

- **Traducir a lenguaje técnico los Requerimientos**: Sumado a una notación adecuada, el lenguaje empleado debe poder ser utilizado en próximas etapas.


