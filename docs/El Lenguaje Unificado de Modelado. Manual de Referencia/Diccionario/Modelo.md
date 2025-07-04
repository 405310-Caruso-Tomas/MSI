>  Arquetipo o punto de referencia. Representación simplificada de un objeto, sistema, proceso o idea que se utiliza para comprender cómo funciona.
- **REPRESENTACIÓN DE UN OBJETO, SISTEMA O IDEA**, de forma diferente al de la entidad misma. 
- A su vez, documenta las decisiones que se han adoptado, por lo que aporta **trazabilidad** entre diferentes modelos 
- El modelo capta los aspectos importantes de lo que se está modelando, desde un cierto punto de vista, y simplifica u omite el resto.
****
Viendo el concepto desde lo que nos compete como desarrolladores, un modelo deberá representar fiel y completamente los [Requerimientos](../../assets/Requerimientos.md) de los usuarios. Además de describir al sistema con suficiente detalle como para hacer predicciones válidas sobre el comportamiento de este.
- Sirve de guía en la construcción de un sistema.
- Una abstracción de la estructura y comportamiento de un sistema.
- Captura las propiedades estructurales (estáticas) y de comportamiento (dinámicas) de un sistema.
****
##### **¿Qué hay en un modelo?**
**Semántica y presentación.** Los modelos tienen dos aspectos principales: la información semántica (semántica) y la presentación visual (notación).
	La **semántica** en un modelo se refiere al significado preciso y consistente de los elementos (clases, objetos, estados), relaciones y diagramas que componen el modelo. Las [Áreas Conceptuales de UML](../../assets/Áreas Conceptuales de UML.md) organizan los diagramas según la semántica que representan, por ejemplo.
	La **presentación visual** se refiere a la notación gráfica o sintaxis visual utilizada para representar los elementos, relaciones y estructuras de un modelo en los diagramas [UML](../../assets/UML.md), por ejemplo.
	Mientras que la **semántica** define el **significado** de los elementos (qué representa una clase, una asociación, etc.), la **presentación visual** define **cómo se dibujan** esos elementos en un diagrama. Por ejemplo:
	- **Semántica**: Una clase representa un conjunto de objetos con atributos y comportamientos comunes.
	- **Presentación visual**: Una clase se representa como un rectángulo dividido en compartimentos (nombre, atributos, operaciones).
**Contexto.** Refiere al entorno, propósito y perspectiva en los que se define y utiliza el modelo. Es el marco que establece los límites, las suposiciones y las condiciones bajo las cuales los elementos del modelo (como clases, objetos, relaciones o comportamientos) tienen significado. Ayuda a delimitar qué se está modelando.
****
##### **¿Para qué sirven los modelos?**
1. **Para capturar los requisitos y el dominio del conocimiento, de forma que todos los implicados puedan entenderlos y estar de acuerdo con ellos.**
2. **Para pensar en el diseño de un sistema.**
3. **Para capturar las decisiones de diseño en un formato alterable.**
4. **Para generar productos usables para el trabajo.**
5. **Para explorar económicamente múltiples soluciones.**
6. **Para dominar sistemas complejos** (complejidad difícil de tratar directamente). 
****
###### **Clasificación**
Existen modelos esquemáticos que abarcan dibujos, mapas y diagramas. Existen modelos simbólicos, los cuales están basados en las matemáticas o en un código de computadora. Incluso modelos físicos tales como el modelo de un avión.
Una forma de clasificarlos es según la forma que representan el **tiempo**:

**ESTÁTICOS**: Un modelo estático omite ya sea un reconocimiento del tiempo o describe un instante del estado de un sistema en determinado momento. Debe proporcionar, y especificar propiedades no cambiantes, de manera que se soporte toda la funcionalidad requerida del Modelo.

**DINÁMICOS**: Un modelo dinámico reconoce explícitamente el transcurso del tiempo. Proporciona una secuencia de estados del sistema en el tiempo. Ciclo de vida de los objetos e interrelaciones que se producen entre los mismos.