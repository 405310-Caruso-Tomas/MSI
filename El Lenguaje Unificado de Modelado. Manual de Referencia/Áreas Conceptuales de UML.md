> Son categorías definidas en la especificación de UML para clasificar diagramas según el tipo de información que modelan (estructura, comportamiento, interacción). Son parte del estándar UML y **se centran en la semántica de los diagramas.**

La **semántica**, la consideramos inherente a un **[[Modelo]]**, y es en ese inciso donde es mencionada.
Son una guía para los modeladores sobre qué diagramas usar según el aspecto del sistema, y con qué elementos.
Los conceptos y modelos de [[UML]] pueden agruparse en las siguientes áreas conceptuales:
****
##### **Estructura estática** 
**[[Clases]], Atributos y Operaciones.** Esta área se centra en cómo están organizados los componentes, relaciones y propiedades de un modelo en un momento dado. 
- Los conceptos son modelados como [[Clases]].
- Varias clases pueden compartir su estructura común utilizando la generalización, herencias.
- Los objetos también tienen conexiones en tiempo de ejecución con otros objetos individuales. Estas relaciones objeto a objeto se modelan mediante **asociaciones** entre clases.
- Las clases pueden tener **interfaces**, los cuales **describen su comportamiento visible desde el exterior**. 
- Los diagramas asociados más comunes a estas áreas son el **[[Diagrama de Clases]], diagrama de objetos** (muestra instancias específicas de clases), **[[Diagrama de Componentes]]**.
****
##### **Construcciones de Diseño**
**Clasificadores, Puertos, Colaboraciones y Componentes.** Describe los elementos que se utilizan en la fase de diseño para modelar la arquitectura y los detalles técnicos de un sistema, orientados a la implementación.
- En la fase de diseño, una clase puede descomponerse en partes (subelementos o instancias internas) que interactúan entre sí.
- Un **[[Clasificador]] estructurado** es una extensión de una clase en UML que permite modelar su estructura interna como una colección de partes conectadas mediante conectores.
- Se suele representar en un **[[Diagrama de Estructura Interna]]**, donde la clase se muestra como un rectángulo que contiene partes internas (rectángulos más pequeños) unidas por líneas (conectores).

- Una clase puede encapsular su estructura interna y exponer solo ciertas interfaces al exterior mediante un **[[Puerto]]** o más de uno.

- **[[Colaboración]]**, **[[Diagrama de Colaboración]]**.

- Un **[[Componente]]** es una parte **modular** y reemplazable de un sistema que implementa un conjunto de interfaces. 
****
##### **Construcciones de Despliegue**
**Nodo, Artefacto, Manifestación y Vista.** Son los elementos utilizados para modelar la distribución física de un sistema en ejecución, es decir, cómo los elementos de software se implementan en el hardware o infraestructura física.
- Un **nodo** es un recurso de cálculo de tiempo de ejecución que define una ubicación física o lógica en la que se ejecutan los elementos de software.
- Modelan los elementos físicos o lógicos donde el software se despliega y ejecuta, como servidores, bases de datos o máquinas virtuales.
- Los nodos pueden conectarse entre sí mediante enlaces (representando redes o canales de comunicación).

- Un **artefacto** representa elementos tangibles del software, como archivos, bibliotecas, bases de datos o scripts, que se despliegan en nodos. Son elementos concretos que resultan del desarrollo.
- Ejemplo: En el sistema de biblioteca, un artefacto podría ser `BibliotecaApp.jar` (un archivo Java ejecutable) o `BaseDatosBiblioteca.sql` (un archivo de base de datos).

- Un **artefacto** puede ser una **manifestación** (es decir, una implementación) de un componente. La **manifestación** es una relación que conecta un artefacto físico con un elemento lógico del diseño.
- La relación de manifestación indica que un artefacto "da vida" a un componente, implementando sus interfaces y comportamiento. 

- La **vista de despliegue** es una perspectiva del sistema que se enfoca en su implementación física, mostrando cómo los nodos (hardware o entornos) están organizados y cómo los artefactos (software) se distribuyen en ellos.
- El **[[Diagrama de Despliegue]]** es el principal vehículo para la vista de despliegue, mostrando nodos como cubos 3D, artefactos como rectángulos, y relaciones como flechas. Además de contener la representación de todos los elementos mencionados.
****
##### **Comportamiento Dinámico**
Elementos y diagramas utilizados para modelar el comportamiento de un sistema, es decir, cómo sus componentes interactúan o cambian de estado.
Intentan capturar la vida de un objeto, las interacciones entre objetos y los flujos de ejecución.
- La **historia de vida de un objeto** muestra cómo este interactúa con el resto del mundo a lo largo de su existencia, enfocándose en sus estados, eventos que lo afectan, acciones que realiza y transiciones entre estados.
- Se representa mediante una **[[Máquina de Estados]]**.
- Por ejemplo, en un sistema de biblioteca, un objeto `Libro` podría tener estados como `Disponible`, `Prestado` y `Reservado`, con transiciones desencadenadas por eventos como "prestar" o "devolver".

- Las **interacciones** describen cómo los objetos (o partes de un clasificador estructurado o colaboración) intercambian mensajes para lograr un objetivo, como ejecutar un caso de uso.
- Se representan en **diagramas de secuencias** y **diagramas de comunicación**. Los diagramas de secuencia hacen énfasis en las secuencias de tiempo, mientras que los diagramas de comunicación hacen mayor hincapié en las relaciones entre objetos.

- Una **actividad** representa [[Flujos de Proceso]], que puede ser secuencial o concurrente, e incluye construcciones como decisiones, bucles y bifurcaciones. 
- Representa la ejecución de un cálculo. Se modela como un conjunto de nodos de actividad conectados mediante flujos de control y flujos de datos.
- **[[Diagrama de Actividad]]** pueden ser utilizados para mostrar estos cálculos.

Un diagrama de **casos de uso** **muestra cómo fluye la interacción entre usuarios y el sistema a lo largo del tiempo**, lo cual es una forma de **comportamiento observable** y no una estructura estática, por lo que se dice que pertenece a esta área conceptual.
****
##### **Organización del Modelo**
Refiere a cómo se estructura la información de modelado para que sea comprensible, manejable y escalable, especialmente en sistemas grandes.
- Los **paquetes** dividen un modelo grande en unidades más pequeñas y comprensibles.
- Son contenedores lógicos que pueden incluir cualquier elemento UML (clases, casos de uso, diagramas) y pueden organizarse jerárquicamente (paquetes dentro de otros paquetes).
- Se representan en un **diagrama de paquetes**. Ejemplo: En un sistema de biblioteca, un paquete `Dominio` podría contener clases como `Libro` y `Usuario`, mientras que un paquete `InterfazUsuario` agrupa elementos relacionados con la interfaz gráfica.

- Una **dependencia entre paquetes** es una relación que indica que los elementos de un paquete (el cliente) dependen de los elementos de otro paquete (el proveedor).
- Una dependencia significa que un cambio en el paquete proveedor puede afectar al paquete cliente, pero no al revés.
- Si el paquete `InterfazUsuario` usa clases del paquete `Dominio`, se dibuja una dependencia de `InterfazUsuario` hacia `Dominio`.
- Las dependencias pueden incluir estereotipos como `<<import>>` (importar elementos del paquete proveedor) o `<<access>>` (acceso directo a elementos).
****
##### **Perfiles**
**Perfiles, Estereotipos, Valores Etiquetados y Restricciones**. Mecanismos de extensibilidad diseñados para personalizar y adaptar el lenguaje a necesidades específicas. Estas construcciones permiten a los usuarios definir nuevos tipos de elementos, agregar atributos personalizados y establecer restricciones adicionales, manteniendo la compatibilidad con el estándar UML.
Un **perfil** es un conjunto de **estereotipos**, **valores etiquetados** y **restricciones** desarrollados con un propósito específico, que puede almacenarse en bibliotecas para su reutilización en diferentes modelos.
- Un **estereotipo** es un nuevo tipo de elemento base. 
- Ejemplo: En un sistema de biblioteca, una clase Libro podría estereotiparse como `<<Persistent>>` para indicar que sus instancias se almacenan en una base de datos. Se aplican a cualquier diagrama UML.

- Un **valor etiquetado** es un atributo definido por el usuario que se aplica a los elementos del modelo.
- Son pares clave-valor asociados a un elemento del modelo, definidos como parte de un estereotipo.
- Los valores etiquetados pueden usarse para indicar prioridad (de forma `{prioridad=alta}`), indicar el nombre de una tabla en base de datos (`{tabla=libros}`), formato de salida (`{formato=JSON}`).

- Una **restricción** es una condición bien formada expresada como una cadena de texto en un lenguaje restrictivo. Las restricciones pueden aplicarse a cualquier elemento UML.
- Ejemplo: En el sistema de biblioteca, una restricción en una clase `Préstamo` podría ser `{OCL: fechaDevolucion >= fechaPrestamo}`, asegurando que la fecha de devolución sea posterior a la de préstamo.
- Object Constraint Language (OCL) es un lenguaje formal para expresar restricciones precisas


