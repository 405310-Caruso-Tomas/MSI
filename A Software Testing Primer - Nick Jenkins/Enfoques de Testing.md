Las pruebas del software pueden ser analizadas desde diferentes enfoques, ofreciendo cada uno una perspectiva distinta sobre cómo ejecutar y evaluar el software. La imagen muestra los enfoques más comunes.
![[Pasted image 20250603102226.png]]
Tener en cuenta que este apartado no se refiere en sí a las pruebas que se realizan, como son detalladas en otros incisos, sino que refiere más a la perspectiva en general que se tiene de estas en conjunto, y su clasificación.
****
#### *Desde su Comportamiento*
Podemos clasificarlas según el comportamiento esperado del sistema al ejecutar las pruebas.
- Distinguimos las ***Pruebas Estáticas.*** Aquellas en las que no se ejecuta el código del software. Se enfocan en revisar el código fuente, la documentación, o el diseño del sistema para identificar defectos sin necesidad de ejecutar el programa. Estos defectos pueden ser errores de sintaxis o malas prácticas de programación, por ejemplo.
- **Pruebas Dinámicas.** Requieren ejecutar el software y observar su comportamiento en tiempo real, para determinar si el software cumple con los requisitos operativos y de rendimiento mientras se ejecuta. 
- **Ejemplo:** Probar la funcionalidad de un formulario de login, verificar si las entradas son procesadas correctamente por el sistema.
****
#### *Desde su Implementación y Ejecución*
Según cómo se implementen y ejecuten las pruebas.
- **Pruebas Manuales.** Implican la intervención de un tester humano que sigue un conjunto predefinido de pasos para probar el software.
- El objetivo es detectar problemas relacionados con la interacción usuario aplicación, experiencia de usuario (UX), y comprobar si el sistema funciona correctamente sin herramientas automatizadas.
- **Ejemplo.** Un tester accede a la página de inicio de sesión, introduce credenciales y verifica si el sistema permite el acceso correctamente.
- **Pruebas Automatizadas.** Se utilizan herramientas de software para ejecutar las pruebas de manera automática. Son ideales para verificaciones repetitivas, y permitir la ejecución de pruebas continua durante TODO el ciclo de vida del software.
- **Ejemplo.** Utilizar herramientas como Selenium para automatizar las pruebas de la interfaz de usuario en una aplicación web.
****
#### *Desde los Requisitos*
Según el tipo de requisitos que se están verificando. Y se divide principalmente en requisitos funcionales o no funcionales.
- **[[Pruebas Funcionales (White Box vs. Black Box)]].** Validan que el software cumpla con las funcionalidades descritas en los documentos de requisitos, y que las características del sistema funcionan de acuerdo con los objetivos de negocio.
- **Ejemplo.** Verificar que un sistema de pago en línea acepte pagos correctamente cuando el usuario ingresa los datos de tarjeta de crédito.
- **Pruebas No Funcionales.** Validan rendimiento, usabilidad, seguridad, accesibilidad, eficiencia, etc. Ayudan a evaluar la calidad general del sistema.
- **Ejemplo.** Pruebas de carga, con grandes volúmenes de usuarios simultáneos.
****
*![[Pasted image 20250603115339.png]]![[Pasted image 20250603115403.png]]*