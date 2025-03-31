> “La ingeniería de software es el establecimiento y uso de principios fundamentales de la ingeniería con objeto de desarrollar en forma económica software que sea confiable y que trabaje con eficiencia en máquinas reales.”

> Es 1. La aplicación de un enfoque sistemático, disciplinado y cuantificable al desarrollo, operación y mantenimiento de software; es decir, la aplicación de la ingeniería al software. Y a su vez, 2. el estudio de enfoques según el punto 1.”
#### ⦁	LA NATURALEZA DEL SOFTWARE
En la actualidad, el software tiene un papel dual. Es un producto y al mismo tiempo es el vehículo para entregar un producto.
La enorme industria del software se ha convertido en un factor dominante en las economías del mundo industrializado. Equipos de especialistas de software, cada uno centrado en una parte de la tecnología que se requiere para llegar a una aplicación compleja, han reemplazado al programador solitario de los primeros tiempos
#### ⦁	Definición de software
El software es elemento de un sistema lógico y no de uno físico. El **software** es un conjunto de instrucciones o programas informáticos que le indican a una computadora cómo realizar tareas específicas.
[[Tipos de Software]]
###### Características del software que lo hacen diferente de otros objetos que construyen los seres humanos:

###### ⦁	El software se desarrolla o modifica con intelecto;  no se manufactura en el sentido clásico.
⦁	El software no se “desgasta”:
	el hardware presenta una tasa de fallas relativamente elevada en una **etapa temprana** de su vida (fallas que con frecuencia son atribuibles a defectos de diseño o manufactura); los defectos se corrigen y la tasa de fallas se abate a un nivel estable durante cierto tiempo. No obstante, conforme pasa el tiempo, la tasa de fallas aumenta de nuevo a medida que los componentes del hardware resienten los efectos acumulativos de suciedad, vibración, abuso, temperaturas extremas y muchos otros inconvenientes ambientales. En pocas palabras, el hardware comienza a desgastarse. 

El software no es susceptible a los problemas ambientales que hacen que el hardware se desgaste, el software no se desgasta, **¡pero sí se deteriora!** .Con el tiempo se vuelve antiguo y puede llegar a denominarse [[Software Heredado]]

![[Pasted image 20250311110055.png]]
- Aunque la industria se mueve hacia la construcción basada en componentes, la mayor parte del software se construye para un uso individualizado: Un componente de software debe diseñarse e implementarse de modo que pueda volverse a usar en muchos programas diferentes. Los modernos componentes reutilizables incorporan tanto los datos como el procesamiento que se les aplica, lo que permite que el ingeniero de software cree nuevas aplicaciones a partir de partes susceptibles de volverse a usar.


## CAPAS de la Ingeniería de Software

![[Pasted image 20250311121355.png]]

La ingeniería de software es una tecnología con varias capas. La ingeniería de software incluye un proceso, métodos y herramientas para administrar y hacer ingeniería con el software.
El fundamento en el que se apoya la ingeniería de software es el ***compromiso con la calidad.*** Aunque las herramientas parecen lo más visible, Pressman enfatiza que la calidad es la raíz de todo, guiando las otras capas.
Incluye atributos de calidad como confiabilidad, eficiencia, mantenibilidad, usabilidad y seguridad. Podemos definir la calidad como el cumplimiento de los requisitos especificados y las expectativas de los usuarios.

[[PROCESO]]: Define cómo se desarrolla el software, usando modelos como Waterfall o Agile. Es como el plan general: define el marco o metodología que se utilizará para el desarrollo. La estructura para organizar las actividades.

##### **MÉTODOS**
Son las técnicas específicas dentro del modelo de proceso seleccionado, como usar diagramas UML para diseñar, pruebas unitarias para verificar el código, TDD (Desarrollo Guiado por Pruebas), entre otros. 
Proporcionan la experiencia técnica para elaborar software, e incluyen tareas como:
	***Comunicación, Análisis de requerimientos, Modelación del Diseño, Construcción del programa, Pruebas y Apoyo.***
Están basados en un conjunto de principios fundamentales que gobiernan cada área de la tecnología. Son las "herramientas conceptuales" que los ingenieros de software utilizan para realizar su trabajo.

#### **HERRAMIENTAS**
Proporcionan un apoyo automatizado o SEMI automatizado para el proceso y los métodos. Herramientas para los métodos
Incluyen programas que ayudan, como Git para controlar versiones, Jira para gestionar tareas o JUnit para pruebas automáticas, o incluso IDEs.

|**Capa**|**Descripción**|**Ejemplo**|
|---|---|---|
|Enfoque en la Calidad|Base que asegura calidad (confiabilidad, usabilidad)|Definir tiempos de respuesta rápidos|
|Proceso|Marco para el desarrollo (Agile, Waterfall)|Elegir Scrum para iteraciones cortas|
|Métodos|Técnicas específicas (TDD, diseño UML)|Usar pruebas unitarias para verificar|
|Herramientas|Soporte técnico (Git, Jira, Selenium)|Usar Git para control de versiones|
#### Comparación con Otros Enfoques y Controversias
Aunque Pressman describe estas cuatro capas específicas, otros autores y modelos de arquitectura de software también utilizan conceptos de "capas" o "niveles", pero con diferentes enfoques:
- En la arquitectura de software, se habla de "arquitectura en capas" (n-tier architecture), que divide el sistema en capas como presentación, lógica de negocio y datos. Esto es diferente de las capas de Pressman, que se centran en el proceso de ingeniería de software en lugar de la arquitectura del producto final.
