Las técnicas de descubrimiento de **[Requerimientos](/Patrones en la Construcción de Modelos Conceptuales para Sistemas de Información/Requerimientos)** son esenciales para identificar las necesidades de los usuarios en proyectos de software.

Todas las diferentes fuentes de requerimientos (participantes, dominio, sistemas) durante el proceso de Adquisición y Análisis de requerimientos se representan como **puntos de vista** del sistema, y cada visión muestra un subconjunto de requerimientos. Es recomendable usar estos puntos de vista para estructurar tanto el descubrimiento como la documentación de los requerimientos del sistema.

> Un **punto de vista** es una forma de recopilar y organizar un conjunto de requerimientos de un grupo de participantes con algo en común. Los puntos de vista pueden provenir de usuarios finales, administradores, etcétera. Ayudan a identificar a los individuos y sus requerimientos y a estructurar los requerimientos para análisis.
****
#### **Entrevistas**
Las entrevistas formales o informales con participantes del sistema son una parte de la mayoría de los procesos de ingeniería de requerimientos. El equipo de ingenieros formula preguntas a los participantes sobre el sistema que actualmente usan y el sistema que se va a desarrollar. Los requerimientos se derivan de las respuestas a dichas preguntas. Las entrevistas pueden ser:
	**Entrevistas cerradas**, donde los participantes responden a un conjunto de preguntas preestablecidas.
	**Entrevistas abiertas**, en las cuales no hay preguntas o agenda predefinida. Los ingenieros exploran un rango de conflictos con los participantes del sistema.
*En la práctica, las entrevistas con los participantes son por lo general una combinación de ambas.*

La efectividad de esta técnica está "librada a la suerte" por la calidad de la conversación, decisiones sobre mencionar o no una cuestión, jerga específica, dificultad para expresarse, malinterpretaciones, qué quiere revelar el entrevistado sobre la estructura y toma de decisiones de la organización, etc...
****
(El siguiente es quizás otro ejemplo de autores que se contradicen, *Sommerville* trata a las [Historias de Usuario](/Users Stories Applied - Mike Cohn/Historias de Usuario) como un tipo de escenario, mientras que en *Users Stories Applied*, el autor dedica un capítulo entero a diferenciar las **H.U** de otras técnicas de descubrimiento de requerimientos. Aunque ambos ejemplifican los escenarios de forma sutilmente diferente).
#### **Escenarios**
Por lo general, las personas encuentran más sencillo vincularse con ejemplos reales que con descripciones abstractas.
Útiles para detallar un bosquejo de descripción de requerimientos. 
Son ejemplos sobre interacciones de forma ***Usuario-Sistema***.
Cada escenario abarca comúnmente una interacción o un número pequeño de interacciones posibles..
Un escenario puede incluir:
	1. Una descripción de qué esperan el sistema y los usuarios cuando inicia el escenario. **SUPOSICIÓN INICIAL**
	2. Una descripción en el escenario del flujo normal de los eventos.
	3. Una descripción de qué puede salir mal y cómo se manejaría.
	4. Información de otras actividades que estén en marcha al mismo tiempo.
	5. Una descripción del estado del sistema cuando termina el escenario.
Estos últimos pueden escribirse como texto, complementarse con diagramas, tomas de pantallas, etcétera.
	![Pasted image 20250518085242.png](/assets/Pasted image 20250518085242.png)
#### **[Caso de Uso](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Caso de Uso)**
Los casos de uso son una técnica de descubrimiento de requerimientos que se introdujo por primera vez en el método *Objectory* (mejor referenciado en el apartado de [Historia de UML](/El Lenguaje Unificado de Modelado. Manual de Referencia/Historia de UML)). Ahora se ha convertido en una característica fundamental del modelado de lenguaje unificado ([UML](/El Lenguaje Unificado de Modelado. Manual de Referencia/UML)). 
**[Diagrama de Casos de Uso](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Casos de Uso)**
****
#### **Etnografía**
Los **sistemas** de software no existen aislados. Se usan en un contexto social y organizacional, y dicho escenario podría derivar o restringir los requerimientos del sistema de software.
La etnografía es una **técnica de observación** que se usa para entender los procesos
operacionales y ayudar a derivar requerimientos de apoyo para dichos procesos. 
Un analista se adentra en el ambiente laboral donde se usará el sistema y toma notas acerca de las tareas existentes en que intervienen los participantes del sistema. 
Ayuda a descubrir requerimientos implícitos del sistema que reflejan las formas actuales en que trabaja la gente, en vez de los procesos formales definidos por la organización. 
La etnografía puede combinarse con la creación de prototipos, de modo que se requieran menos ciclos de refinamiento del prototipo.
Sin embargo, debido a su enfoque en el usuario final, no siempre es adecuado para descubrir requerimientos de la organización o de dominio. En consecuencia, la etnografía debe usarse para complementar otros enfoques, como uno de los mencionados más arriba.