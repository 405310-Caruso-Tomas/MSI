**El propósito de informar un defecto es conseguir que se solucione.**
> *Un informe de defectos mal redactado supone una pérdida de tiempo y esfuerzo para muchas personas. Un informe conciso y descriptivo permite eliminar un error de la forma más sencilla posible.*

Además, para los testers, los informes de defectos representan el principal resultado de su trabajo. 
Los informes de defectos van más allá de su uso inmediato. Pueden incluso transmitirse a diversos niveles de gestión dentro de diferentes organizaciones. 
	![[Pasted image 20250524154649.png]]
Existen ciertas características deseables para este reporte, entre ellas está que sea **OBJETIVO**, **ESPECÍFICO** (un informe por defecto), **CONCISO** (simple y directo), **REPRODUCIBLE** (suficiente información para que cualquier persona pueda repetir/ver claramente el problema), **EXPLÍCITO** (información clara), **PERSUASIVO** (redactado de forma que promueva a los desarrolladores a corregir el problema). 
****
> *Un informe de defecto escrito sin aislarlo ni generalizarlo es un defecto informado a medias.*

**ISOLACIÓN.** Es el proceso de examinar las causas del defecto.
Es importante separar los síntomas del problema de su causa. El aislamiento de un defecto generalmente se realiza haciendo que se manifieste varias veces en diferentes situaciones para comprender cómo y cuándo ocurre.

**GENERALIZACIÓN.** Es el proceso de entender de forma amplia el impacto del defecto.
Como sabemos, los desarrolladores reutilizan código y esto provoca que un error presente en una porción de código afecte a varios módulos del sistema. Quienes registren defectos deben intentar extrapolar dónde podría ocurrir un problema para que el desarrollador considere el contexto completo del defecto, no solo un incidente aislado.
****
Cuando un defecto es detectado, se documenta con un conjunto de atributos clave que permiten su gestión y resolución, entre ellas:
- **ID**. Número único que identifica el defecto.
- **Nombre.** Breve descripción.
- **Severidad.** Impacto del defecto en el sistema.
- **Prioridad.** Urgencia con la que debe corregirse.
****
##### **Severidad**
> La severidad mide el impacto del defecto en la funcionalidad del sistema o experiencia del usuario. 

Podemos clasificar la severidad de los defectos en **Severidad-1** (impide la finalización del proyecto) y **Severidad-2** (defectos que en cantidades limitadas permiten que el proyecto se complete).
También podemos clasificarlos en función de:
- ***Impacto (Alto/Bajo).*** Gravedad del defecto cuando ocurre.
- ***Probabilidad (Alta/Baja).*** Frecuencia con la que es probable que ocurra el defecto.
 ![[Pasted image 20250524160613.png]]
****
##### **Prioridad**
 La prioridad indica qué tan urgente es corregir el defecto. Un defecto menor en una pantalla poco usada es diferente en prioridad a un defecto crítico en un sistema de pagos.
 Cuando se tiene un defecto, es importante determinar si debe corregirse inmediatamente, esto determina la prioridad del mismo. Se suelen clasificar en:
 - ***Alta.*** Debe resolverse dentro de un día hábil. Afecta la funcionalidad principal o bloquea múltiples casos de prueba.
 - ***Media.*** Pueden ser solucionados dentro del ciclo normal de desarrollo ya que no bloquean la aplicación. *Un defecto en una funcionalidad no crítica y que puede corregirse en una versión futura*, por ejemplo.
 - ***Baja.*** No afecta la funcionalidad, y tiene soluciones alternativas. Se debe corregir luego de otros problemas más importantes. *Un icono que no se alinea correctamente en una interfaz de usuario*, por ejemplo. 
****
##### **Estado de un Defecto***
![[Pasted image 20250524161042.png]]
***Estados comunes en el ciclo de vida de un defecto***.
1. **Nuevo.** Un tester ha identificado y reportado un nuevo defecto, el cual está pendiente de ser asignado a un desarrollador para sus resolución.
2. **Asignado.** Un desarrollador es responsable de investigarlo y solucionarlo.
3. **Rechazado.** El desarrollador lo ha considerado inválido.
4. **Solucionado.** El desarrollador ha corregido el defecto.
5. **Listo para la prueba.** El código corregido fue incorporado, y es accesible para el tester para que este verifique que realmente fue corregido.
6. **Reprueba fallida.** Luego de rehacer pruebas, el tester descubre que el defecto sigue presente, y es devuelto al equipo de desarrollo.
7. **Cerrado.** El defecto fue corregido y ha pasado las pruebas de validación.
También hay flujos diferentes que el defecto puede tomar, por ejemplo:
- **Diferido.** La corrección del mismo fue postergada, para un próximo sprint o versión futura.
- **Duplicado.** El mismo ya fue reportado previamente y se encuentra en proceso de resolución o ya ha sido resuelto.

