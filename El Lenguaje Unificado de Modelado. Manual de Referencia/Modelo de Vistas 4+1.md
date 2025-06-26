El **modelo de vistas 4+1** es un **marco conceptual** utilizado en ingeniería de software, propuesto por *Philippe Kruchten* en 1995, para describir la arquitectura de un sistema de software **desde múltiples perspectivas** o **"vistas".**
****
*Kruchten* argumenta que una sola vista arquitectónica no puede capturar la complejidad de un sistema de software, ya que las partes interesadas (desarrolladores, gerentes, clientes, administradores de sistemas) tienen preocupaciones distintas.
El modelo propone que un sistema software se ha de documentar y mostrar (tal y como se propone en el estándar *IEEE 1471-2000*) con **4 vistas** bien **diferenciadas**. 
Kruchten enfatiza que el modelo 4+1 no es un proceso de diseño, sino un marco para describir la arquitectura. No dicta cómo diseñar el sistema, sino cómo comunicarlo.
El nombre "*4+1*" se refiere a cuatro vistas principales más una vista adicional que las unifica, que es la **vista de escenario**.
![[Pasted image 20250625174843.png]]
****
#### **Las Cuatro Vistas Principales**
**Vista Lógica/Diseño (Logical View)**
- Representa la descomposición funcional del sistema, enfocándose en los elementos que proveen la funcionalidad requerida por los usuarios finales.
- Representa la estructura del sistema en términos de sus **componentes** funcionales, como **[[Clases]]**, objetos, **interfaces** o **módulos**. **[[Colaboración]]** entre clases.
- **Audiencia**: Diseñadores, usuarios finales y analistas de sistemas.
- **Diagramas UML asociados:** **[[Diagrama de Clases]]**, diagramas de objetos, **[[Diagrama de Secuencia]]**,

**Vista de Implementación (Implementation View)**
- Describe cómo se organiza el sistema en términos de **[[Artefacto]]s** físicos, como archivos de código, bibliotecas, ejecutables o componentes desplegables. 
- Se centra en la estructura del software implementado, la organización del software desde la perspectiva del desarrollo. 
- **Audiencia:** Desarrolladores, gestores de configuración, arquitectos.
- **Diagramas UML asociados**: **[[Diagrama de Componentes]]**, **[[Diagrama de Paquetes]]**.

**Vista de Proceso (Process View)**
- Representa el comportamiento dinámico del sistema, incluyendo **[[PROCESO]]S**, hilos, **[[Interacción]]es** entre **[[Componente]]s** y concurrencia. 
- Refiere a la **sincronización de procesos.**
- **Audiencia:** Integradores, desarrolladores 
- Se centra en aspectos como rendimiento, escalabilidad y tolerancia a fallos.
-  **[[Diagrama de Actividad]]**, **[[Diagrama de Comunicación]]**.

**Vista Física (Physical View)**
- Describe cómo los **componentes** del software se mapean/distribuyen a la **infraestructura** física, como servidores, nodos, redes y dispositivos. Se centra en la topología del sistema y su despliegue.
- **Audiencia**: Administradores de sistemas, ingenieros de infraestructura, integradores.
- **[[Diagrama de Despliegue]]**.
****
##### **La Vista Adicional: Vista de Escenarios (Scenarios View o +1)**
Esta vista **unifica** las otras cuatro vistas al describir **[[Caso de Uso]]** o escenarios clave que ilustran cómo los elementos de las vistas lógica, de implementación, de proceso y de despliegue **interactúan** para cumplir con los requisitos del sistema. **Es la "vista integradora".**
Por lo tanto, la audiencia de esta vista serían todas las partes interesadas.
- **Diagramas UML asociados**: **[[Diagrama de Casos de Uso]]**.
- **Ejemplo**: Un escenario como "*Usuario realiza un préstamo de libro*" mostraría cómo el usuario interactúa con la interfaz (vista lógica), cómo se ejecuta el proceso (vista de proceso), qué componentes se usan (vista de implementación) y en qué nodos se ejecuta (vista de despliegue).
****
**Resumen adicional.**
El modelo 4+1 utiliza diagramas UML para representar cada vista, asegurando que cada perspectiva sea clara para las partes interesadas relevantes:
- **Vista Lógica**: Enfocada en la funcionalidad (UML: clases, objetos).
- **Vista de Implementación**: Enfocada en la construcción del software (UML: componentes).
- **Vista de Proceso**: Enfocada en el comportamiento dinámico (UML:  actividad).
- **Vista de Despliegue**: Enfocada en la infraestructura (UML: despliegue).
- **Vista de Escenarios**: Une todo con casos de uso (UML: casos de uso).