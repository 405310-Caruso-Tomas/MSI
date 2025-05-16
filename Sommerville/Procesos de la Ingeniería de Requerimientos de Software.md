![[Pasted image 20250315162204.png]]

(cap 2. pag 38) Los procesos de ingeniería de requerimientos incluyen cuatro actividades de alto nivel. Éstas se enfocan en:
	![[Captura de pantalla de 2025-03-31 12-12-16.png]]

#### **Estudio de Factibilidad**. 
Valorar si el sistema es útil para la empresa (o cliente final), y si las necesidades identificadas del usuario se cubren con las actuales tecnologías de software y hardware. Se considera el costo-beneficio del sistema desde un punto de vista empresarial. Debe responder tres preguntas clave: 
	a) **¿El sistema contribuye con los objetivos globales de la organización?** 
	b) **¿El sistema puede implementarse dentro de la fecha y el presupuesto usando la tecnología actual?** 
	c) **¿El sistema puede integrarse con otros sistemas que se utilicen?**

#### **Adquisición y Análisis**. 
Descubrir requerimientos. Actividad centrada en la gente, los ingenieros de software trabajan con clientes y usuarios finales del sistema para descubrir el dominio de aplicación, qué servicios debe proporcionar el sistema, el desempeño requerido de éste, las restricciones de hardware, etcétera. La interacción es a través de entrevistas y observaciones. Pueden usarse prototipos para ayudar a los participantes a entender cómo será el sistema. Los participantes varían desde administradores y usuarios finales hasta reguladores, quienes certifican la aceptabilidad del sistema.
	![[Pasted image 20250401115756.png]]
	Las actividades del proceso son:
	1. **Descubrimiento de requerimientos**. Éste es el proceso de interactuar con los participantes del sistema para descubrir sus requerimientos.
	2. **Clasificación y organización de requerimientos**. Esta actividad organiza los requerimientos en grupos coherentes. Generalmente se agrupan en subsistemas en base a un modelo de la arquitectura del sistema.
	3. **Priorización y negociación de requerimientos**. Esta actividad se preocupa por priorizar los requerimientos, así como por encontrar y resolver conflictos de requerimientos mediante la negociación.
	4. **Especificación de requerimientos.** Los requerimientos se documentan e ingresan en la siguiente ronda de la espiral. Pueden producirse documentos de requerimientos formales o informales.

La adquisición y el análisis de requerimientos es un proceso iterativo con retroalimentación continua de cada actividad a otras actividades. La comprensión de los requerimientos por parte del analista mejora con cada ronda del ciclo. El ciclo concluye cuando está completo el documento de requerimientos. 

Durante esta etapa existen diferentes [[Técnicas de Descubrimiento de Requerimientos]] utilizadas comúnmente por los ingenieros.
#### **Especificación**. 
Proceso de convertir dichos requerimientos en alguna forma estándar: El [[Documento de Requerimientos del Sistema]] (llamado en ocasiones especificación funcional). Estos requerimientos deben ser claros, completos, y con demás características detalladas en el apartado dedicado a [[Requerimientos]].

#### **Validación**. 
Comprobar que los requerimientos definan realmente el sistema que quiere el cliente. Esta actividad analiza la especificación a fin de garantizar que todos ellos han sido enunciados sin ambigüedades; que se corrigieron inconsistencias, y que los productos del trabajo se presentan conforme a los estándares establecidos. El mecanismo principal de validación de los requerimientos es la [[Revisión Técnica]]. 
Durante este proceso, se realizan diferentes tipos de validaciones al documento:
	1. **De validez**: ¿Las funciones especificadas son las requeridas?
	2. **De consistencia**: Los requerimientos no deben estar en conflicto.
	3. **De totalidad**: El documento debe definir todas las funciones y restricciones pretendidas por el usuario del sistema.
	4. **De realismo**: ¿Las funciones pueden implementarse?
	5. **Verificabilidad**: Se debe poder escribir pruebas que demuestren que el sistema entregado cumpla cada requerimiento especificado. Verificables.

Es difícil demostrar que un conjunto de requerimientos no cubre las necesidades de los usuarios. Para ello, estos últimos necesitan una imagen del sistema en operación. Como resultado, *rara vez usted encontrará todos los problemas de requerimientos durante el proceso de validación de requerimientos.*
****
##### ***Administración de Requerimientos***
Prácticamente en todos los sistemas cambian los requerimientos. Al proceso de administrar tales requerimientos cambiantes se le llama [[Administración de Requerimientos]].
