El término **[Metodología](/MSI/MSI/Metodología)**, sugiere la existencia y descripción de métodos estructurados, los cuales tienen por objetivo ayudar a desarrollar modelos de sistemas en forma sistemática.

Las vistas en este inciso tienen como objetivo ayudar a desarrollar modelos de sistemas en forma sistemática. Reduciendo la ambigüedad de los requerimientos por parte del cliente.
****
#### 1. **Modelado Entidad-Relación (ER)**
 **Descripción**: Es una de las metodologías más utilizadas para diseñar bases de datos y sistemas de información. Se centra en identificar entidades (objetos del mundo real) y las relaciones entre ellas.

- **Elementos clave**: Entidades, atributos, relaciones y cardinalidades.
- **Ejemplo de patrón**: "Cliente" o "Pedido" y sus relaciones como "realiza".
****
#### 2. **[Proceso de Desarrollo Unificado (PUD)](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Proceso de Desarrollo Unificado (PUD))**
****   
#### 3. **Metodología de Análisis Estructurado**
**Descripción**: Se basa en descomponer el sistema en procesos y flujos de datos, utilizando herramientas como el Diagrama de Flujo de Datos (DFD).
    
- **Elementos clave**: Procesos, almacenes de datos, flujos de datos y entidades externas.
- ![Pasted image 20250331105252.png](/MSI/assets/Pasted image 20250331105252.png)
- **Patrón**: Representación jerárquica de niveles (contexto, nivel 0, nivel 1, etc.).
****
#### 4. **Patrones de Modelado Conceptual Específicos**
**Patrón CRUD**: Representa las operaciones básicas (Crear, Leer, Actualizar, Eliminar) en sistemas de información.
    - **Patrón MVC (Modelo-Vista-Controlador)**: Separa la lógica del sistema en tres componentes para facilitar el diseño y mantenimiento.
****
###### **Enfoque según el contexto**
La elección de la metodología depende del propósito del modelado:

- Si es para bases de datos, el modelo ER es predominante.
- Si es para software orientado a objetos, UML es más adecuados.
- Para sistemas centrados en procesos, el análisis estructurado con DFD es común.
****
###### **Características deseables de las metodologías y herramientas**
- **Modelado iterativo y evolutivo**: Las actividades de elicitación, especificación y validación deberían ser repetidas varias veces en un proceso iterativo, de forma que los requerimientos sean refinados y evolucionen, como es detallado en el apartado de [Ingeniería de Requerimientos](/MSI/Sommerville/Ingeniería de Requerimientos). 

- En cada iteración el Modelo debe permitir identificar el origen del requerimiento, y el versionado actual de los mismos. De forma que figure como un seguimiento durante todo el proceso de modelado, hasta su efectivo cumplimiento plasmado en la funcionalidad del Modelo.

- **Diferentes vistas**: vistas que son importantes que estén presentes en cualquier conjunto de metodologías para facilitar la comprensión del sistema: vista *estática, dinámica y funcional* (especifica en forma declarativa, cómo en cada servicio, ante un estímulo, se producen los cambios de estados en sus atributos.)

- **Documentación proporcionada por el Modelo**: La misma debe estar destinada al cliente de manera que certifique los requisitos a satisfacer, y que a su vez, sirva como insumo en las restantes etapas de construcción del sistema.

- **Flexibilidad para cambio de Requisitos**: El Modelo debe ser flexible, permitiendo introducir cambios. Y a su vez, se debe realizar una evaluación de impacto que producirá en el resto del sistema la modificación introducida.

- **Notación favorable**: El lenguaje natural es inherentemente ambiguo, por lo tanto, se deberá procurar llevar a una notación que permita reducir la ambigüedad y unificar el léxico empleado por el usuario, en lo posible.

- **Traducir a lenguaje técnico los Requerimientos**: Sumado a una notación adecuada, el lenguaje empleado debe poder ser utilizado en próximas etapas.


