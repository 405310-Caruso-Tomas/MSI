
> [!Sommerville 1999]
> "Los requerimientos pueden tomar la forma de restricciones sobre los procesos de desarrollo del sistema"

La primera clasificación para los requerimientos la podemos hacer en base a *qué* o *quién* pertenecen:  Podemos distinguir los “requerimientos del **usuario**” para representar los requerimientos abstractos de alto nivel; y “requerimientos del **sistema**” para caracterizar la descripción detallada de lo que el sistema debe hacer:
	- Los requerimientos del **usuario** son enunciados, en un lenguaje natural junto con diagramas, acerca de qué servicios esperan los usuarios del sistema. Deben describir los requerimientos funcionales y no funcionales de forma comprensible. 
	...
	- Los requerimientos del **sistema** son descripciones de las funciones, los servicios y las restricciones operacionales del sistema. Son versiones extendidas de los requerimientos del usuario que los desarrolladores usan como punto de partida. Idealmente, no deben ocuparse de cómo se diseña o implementa el sistema. Especificaciones completas y detalladas de todo el sistema, que pueden ser incluídas como parte del contrato para la implementación del sistema.
	![[Pasted image 20250325101833.png]]

La segunda clasificación refiere más específicamente al comportamiento y performance del sistema, entre Requerimientos Funcionales y No Funcionales:
	2.2.2.1 ***Requerimientos Funcionales***. Definen las funciones que el sistema será capaz de realizar. Describen las transformaciones que el sistema deberá realizar sobre las entradas para producir las salidas. Pueden referirse también a lo que el sistema no debe hacer. Cómo debe comportarse el sistema en situaciones específicas.
	2.2.2.2  ***Requerimientos No Funcionales***. refieren a características que de una u otra forma pueden limitar al sistema como, por ejemplo: el rendimiento, interfaces de usuario, fiabilidad, mantenimiento, seguridad, portabilidad, estándares, etc. Se refieren a propiedades emergentes del sistema. **Una falla de un requerimiento de este tipo podría inutilizar un sistema**. Limitaciones impuestas por los estándares.
![[Pasted image 20250325105644.png]]
	 
Gracias al diagrama, podemos ver que los requerimientos no funcionales provienen de características requeridas del software (requerimientos del producto), la organización que desarrolla el software (requerimientos de la organización) o de fuentes externas:

**Requerimientos del *producto*:** especifican o restringen el comportamiento del software. Los ejemplos incluyen requerimientos de rendimiento sobre qué tan rápido se debe ejecutar el sistema y cuánta memoria requiere.

**Requerimientos de la *organización*:** derivados de políticas y procedimientos en la organización del cliente y del desarrollador. cómo se usará el sistema, requerimientos del proceso de desarrollo que especifican el lenguaje de programación, estándares del entorno, y requerimientos ambientales que definen el entorno de operación del sistema.

**Requerimientos *externos*:** derivados de factores externos al sistema. En ellos se incluyen requerimientos regulatorios que establecen lo que debe hacer el sistema para ser aprobado en su uso por un regulador, o agente externo a la organización o proyecto.

*MHC-PMS como sistema a desarrollar*
![[Pasted image 20250325111222.png]]

Siempre que sea posible, **se deberán escribir de manera cuantitativa los requerimientos no funcionales**, de manera que puedan ponerse objetivamente a prueba. La siguiente figura muestra las métricas que se utilizan para especificar propiedades no funcionales del sistema.
	![[Pasted image 20250325111528.png]]
	Aunque en la práctica, los usuarios de un sistema suelen encontrar difícil traducir sus metas en requerimientos mensurables. Para algunas metas, como la mantenibilidad, no hay métricas para usarse.
****
###### Conflictos entre requerimientos
Los requerimientos no funcionales entran a menudo en conflicto e interactúan con otros requerimientos funcionales o no funcionales. Por ejemplo, el requerimiento de autenticación para el sistema *MHC-PMS* requiere, indiscutiblemente, la instalación de un lector de tarjetas en cada computadora unida al sistema. Sin embargo, podría haber otro requerimiento que solicite acceso móvil al sistema desde las computadoras portátiles de médicos o enfermeras. Esto se conoce como un problema de entendimiento durante la tarea de Indagación en la ingeniería de requerimientos.

