![Pasted image 20250315162204.png](/assets/Pasted image 20250315162204.png)
****
Los **[PROCESO](/R. Pressman/PROCESO)S** de **ingeniería** de **requerimientos** incluyen cuatro actividades de alto nivel. Éstas se enfocan en:
	![Captura de pantalla de 2025-03-31 12-12-16.png](/assets/Captura de pantalla de 2025-03-31 12-12-16.png)
****
#### **Estudio de [Factibilidad](/PMBOK/Factibilidad)** 
**Valorar** si el sistema es útil para la empresa (o cliente final), y si las necesidades identificadas del usuario se cubren con las actuales **tecnologías** de software y **hardware**. 
****
#### **Adquisición y Análisis** 
Descubrir **requerimientos**. Actividad centrada en la gente. 
Los ingenieros de software trabajan con clientes y usuarios finales del sistema para descubrir el **[Modelo de Dominio](/El Lenguaje Unificado de Modelado. Manual de Referencia/Modelo de Dominio)**, **qué** **servicios** debe proporcionar el **sistema**, el **desempeño** requerido de éste, las **restricciones** de hardware, etcétera. 
	![Pasted image 20250401115756.png](/assets/Pasted image 20250401115756.png)
	Las actividades del proceso son:
	1. **Descubrimiento de requerimientos**. Éste es el proceso de interactuar con los participantes del sistema para descubrir sus requerimientos.
	2. **Clasificación y organización de requerimientos**. Esta actividad organiza los requerimientos en grupos coherentes. Generalmente se agrupan en subsistemas en base a un modelo de la arquitectura del sistema.
	3. **Priorización y negociación de requerimientos**. Esta actividad se preocupa por priorizar los requerimientos, así como por encontrar y resolver conflictos de requerimientos mediante la negociación.
	4. **Especificación de requerimientos.** Los requerimientos se **documentan** e ingresan en la siguiente ronda de la espiral. Pueden producirse documentos de requerimientos formales o informales.

La adquisición y el análisis de requerimientos es un **proceso** **iterativo** con **retroalimentación** continua de cada actividad a otras actividades. La comprensión de los requerimientos por parte del analista mejora con cada ronda del ciclo. El ciclo concluye cuando está completo el documento de requerimientos. 

Durante esta etapa existen diferentes **[Técnicas de Descubrimiento de Requerimientos](/Sommerville/Técnicas de Descubrimiento de Requerimientos)** utilizadas comúnmente por los ingenieros.
****
#### **Especificación**. 
**Proceso de convertir dichos requerimientos en alguna forma estándar: El [Documento de Requerimientos del Sistema (ERS)](/Sommerville/Documento de Requerimientos del Sistema (ERS)) (llamado en ocasiones especificación funcional).** 
- Esfuerzo colaborativo que involucra a analistas, clientes, usuarios, desarrolladores y gerentes. 
- En principio, **se debe excluir la información de diseño durante este proceso,** pero si se trata de especificar por completo un software complejo, o con mucha interacción con el hardware, es casi imposible no mencionar al diseño del sistema. 
Se pueden dar casos donde se tenga que diseñar una arquitectura inicial del sistema para estructurar mejor la especificación de requerimientos. 

Es un compromiso **entre** la comunicación de cómo será el sistema para los clientes, la definición precisa del mismo para desarrolladores y examinadores, y la inclusión de **[Información](/Principios de Sistemas de Información - Ralph Stair y George Reynolds/Información)** sobre la posible evolución del **sistema**, para evitar decisiones de diseño restrictivas a futuro.
****
#### **Validación**. 
- Comprobar que los **[Requerimientos](/Patrones en la Construcción de Modelos Conceptuales para Sistemas de Información/Requerimientos)** **definan** realmente el sistema que quiere el cliente.
- Y que los **[Requerimientos](/Patrones en la Construcción de Modelos Conceptuales para Sistemas de Información/Requerimientos)** cumplan con sus características deseables.
Esta actividad **analiza** la **especificación** a fin de garantizar que todos ellos han sido enunciados sin ambigüedades; que se corrigieron inconsistencias, y que los productos del trabajo se presentan conforme a los estándares establecidos. 
- El mecanismo principal de validación de los requerimientos es la **[Revisión Técnica](/R. Pressman/Revisión Técnica)**. 
Durante este proceso, se realizan diferentes tipos de **validaciones** al documento:
	1. **De validez**: ¿Las funciones especificadas son las requeridas?
	2. **De consistencia**: Los **requerimientos** no deben estar en conflicto.
	3. **De totalidad**: El documento debe definir todas las funciones y restricciones pretendidas por el usuario del sistema.
	4. **De realismo**: ¿Las funciones pueden implementarse?
	5. **Verificabilidad**: Se debe poder escribir pruebas que demuestren que el sistema entregado cumpla cada requerimiento especificado. Verificables.

Es difícil demostrar que un conjunto de requerimientos no cubre las necesidades de los **usuarios**. Para ello, estos últimos necesitan una imagen del **sistema** en operación. Como resultado, *rara vez usted encontrará todos los problemas de requerimientos durante el proceso de validación de requerimientos.*
****
##### **Administración de Requerimientos**
Prácticamente en todos los sistemas cambian los requerimientos. Al proceso de administrar tales requerimientos cambiantes se le llama [Administración de Requerimientos](/Sommerville/Administración de Requerimientos).
