(más info en capitulo 6, 7 y demas de r.pressman Modelado de los requerimientos p.157)
El término **[[Metodología]]**, sugiere la existencia y descripción de métodos estructurados, los cuales tienen por objetivo ayudar a desarrollar Modelos de sistemas en forma sistemática. Las vistas en este inciso tienen como objetivo ayudar a desarrollar modelos de sistemas en forma sistemática. Reduciendo la ambigüedad de los requerimientos por parte del cliente.

1. **Modelado Entidad-Relación (ER)**
    - **Descripción**: Es una de las metodologías más utilizadas para diseñar bases de datos y sistemas de información. Se centra en identificar entidades (objetos del mundo real) y las relaciones entre ellas.
    - **Elementos clave**: Entidades, atributos, relaciones y cardinalidades.
    - **Ejemplo de patrón**: "Cliente" o "Pedido" y sus relaciones como "realiza".
    
2. **Modelado Orientado a Objetos (UML)**
    - **Descripción**: El Lenguaje Unificado de Modelado ([[UML]]) es un método estandarizado que utiliza diagramas para representar sistemas de información desde una perspectiva orientada a objetos.
    
3. **Metodología de Análisis Estructurado**
    - **Descripción**: Se basa en descomponer el sistema en procesos y flujos de datos, utilizando herramientas como el Diagrama de Flujo de Datos (DFD).
    - **Elementos clave**: Procesos, almacenes de datos, flujos de datos y entidades externas.
    - ![[Pasted image 20250331105252.png]]
    - **Patrón**: Representación jerárquica de niveles (contexto, nivel 0, nivel 1, etc.).
    
4. **Patrones de Modelado Conceptual Específicos**
    - **Patrón CRUD**: Representa las operaciones básicas (Crear, Leer, Actualizar, Eliminar) en sistemas de información.
    - **Patrón MVC (Modelo-Vista-Controlador)**: Separa la lógica del sistema en tres componentes para facilitar el diseño y mantenimiento.

### Enfoque según el contexto
La elección de la metodología depende del propósito del modelado:
- Si es para bases de datos, el modelo ER es predominante.
- Si es para software orientado a objetos, UML es más adecuados.
- Para sistemas centrados en procesos, el análisis estructurado con DFD es común.