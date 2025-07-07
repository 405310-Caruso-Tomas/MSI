> Un par etiqueta valor, conectado a un elemento del modelo para contener información.

Un valor etiquetado es una pareja valor nombre, que puede conectarse a un elemento del modelo, que usa un [Estereotipo](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Estereotipo).

Los valores etiquetados suelen estar vinculados a **estereotipos**, que definen qué etiquetas son válidas y qué tipo de valores pueden tomar.

- Representan información de modelado adicional. Una extensión a los metaatributos de las metaclases de UML.
- Esta información adicional puede ser útil para el beneficio de herramientas de soporte, tales como generadores de código, de informes y simuladores.
- Puede aplicarse a cualquier **elemento** UML, como [Clases](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Clases), atributos, operaciones, o incluso estereotipos definidos en un perfil UML.
****
##### **Notación**
Cada valor etiquetado se muestra en la forma `{etiqueta=valor}`.
Una clase `Producto` con el estereotipo `<<entity>>` podría tener valores etiquetados:

![Pasted image 20250623192559.png](/MSI/assets/Pasted image 20250623192559.png)

Aquí, `{tabla=productos}` indica que la clase se mapea a una tabla llamada "productos" en la base de datos, y `{version=2.1}` especifica la versión del modelo.
Una relación entre dos clases podría tener un valor etiquetado como `{cascade=true}` para indicar que las operaciones en una clase afectan a la otra.