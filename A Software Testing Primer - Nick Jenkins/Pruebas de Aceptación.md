Los proyectos de software a gran escala a menudo tienen una fase final de pruebas llamada 'Pruebas de Aceptación'.
Otras pruebas, como las unitarias o de integración, pueden realizarse de manera iterativa y con mayor libertad para ajustar el código, ya que se ejecutan en etapas intermedias del desarrollo. Las pruebas de aceptación, por otro lado, suelen ser la última barrera antes de la entrega al cliente o usuario final.
****
- El objetivo es asegurarse de que el sistema cumple con los requisitos acordados que el usuario necesita y es apto para su uso en el mundo real.
- Se realizan en un entorno lo más similar posible al de producción.
- Su propósito es **validar si el producto es aceptado**. Por lo que tiene un enfoque especial en el usuario.
- Se llevan a cabo **después de que el sistema haya sido completamente desarrollado, probado en niveles previos** (unitarios, integración, sistema), y está listo para ser entregado en su versión final.
- También se evalúa si el sistema es fácil de usar, intuitivo y de acuerdo con las expectativas del cliente.
****
###### **¿Qué se hace en las pruebas de aceptación?.** 
Estas pruebas son cuidadosamente planificadas y documentadas: siguen un conjunto predefinido de [[Casos de Prueba]] basados en los requisitos del cliente o usuario final. Se evalúa al sistema bajo condiciones de uso típicas, y obviamente para que las funcionalidades esenciales estén operativas.
En muchos proyectos, especialmente en contratos con clientes externos, las pruebas de aceptación están vinculadas a acuerdos legales. Si se encuentran defectos durante estas pruebas, puede haber consecuencias contractuales, como la obligación de corregir los errores sin costo adicional, retrasos en la entrega o penalizaciones.
****
###### **¿Quién realiza las pruebas de aceptación?.** 
Las pruebas de aceptación son **realizadas principalmente por los usuarios finales o representantes del cliente**. El equipo de pruebas de calidad (QA) o desarrollo no suele estar directamente involucrado en esta fase, ya que el objetivo es evaluar el software desde la perspectiva del usuario final.
****
###### **Tipos de Pruebas de Aceptación**
- ***Pruebas de Aceptación del Usuario (UAT).*** El tipo más común de prueba de aceptación, donde los usuarios finales prueban el sistema para verificar que cumple con sus requisitos y expectativas.
- ***Pruebas de Aceptación Operacional (OAT).*** Se evalúan aspectos operacionales del sistema, como su capacidad de operar correctamente en el entorno de producción, la seguridad, la gestión de fallos y la recuperación.
	- **Ejemplo.** 
- ***Pruebas de Aceptación Contractual.*** Aseguran que el producto cumpla con todas las leyes, reglas de seguridad o estándares establecidos en el contrato entre el cliente y el proveedor.
	- **Ejemplo.** Un sistema de gestión de datos personales se somete a pruebas de aceptación para asegurarse de que cumple con la normativa GDPR sobre la protección de datos personales.
- ***Pruebas de Aceptación de Negocio (BAT).*** ¿El sistema entrega valor desde el punto de vista empresarial?.
	- **Ejemplo.** Una plataforma de comercio electrónico es probada para asegurarse de que las funcionalidades se alineen con las metas de negocio de la empresa.
- ***Pruebas de Aceptación de Usabilidad.*** Evalúan la facilidad de uso, experiencia del usuario (UX), interfaz de usuario (UI), accesibilidad.
****
###### ***ALPHA Vs. BETA TESTING***. 
Otros tipos de pruebas comunes de nombrar a la hora de hablar de pruebas de aceptación son el [[Alpha vs. Beta Testing]]. Estas requieren dos preconceptos para ser mejor entendidas.
