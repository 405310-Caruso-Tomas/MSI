> **Mecanismo** de uso general para **organizar** **elementos** en **grupos**, **estableciendo propiedades** de elementos, y proveyendo **nombres únicos** para hacer referencia a los elementos.

**Agrupación** de elementos del **modelo** y diagramas, **similar a una carpeta en un sistema de archivos.**
Un **paquete** puede poseer cualquier clase de elemento del modelo (clases, casos de uso, diagramas).

- Un **paquete** puede contener además, **paquetes anidados**. Normalmente hay un **paquete** raíz que posee al modelo completo de un sistema.
- Su propósito principal es estructurar el modelo de manera **modular**.
- Se usa en diversos **diagramas UML**, como **[Diagrama de Clases](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Clases)**, **[Diagrama de Casos de Uso](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Casos de Uso)**, **[Diagrama de Componentes](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Componentes)** o [Diagrama de Despliegue](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Despliegue), **[Diagrama de Paquetes](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Paquetes)** y también a nivel de modelo general.
- Un paquete define la **visibilidad** de sus elementos contenidos como **privado** o **público**.
- También son unidades para cualquier mecanismo de control de versiones.
****
Una **dependencia entre paquetes** es una relación que indica que los elementos de un paquete (el cliente) dependen de los elementos de otro paquete (el proveedor).

Una dependencia significa que un cambio en el paquete proveedor puede afectar al paquete cliente, pero no al revés.
Las dependencias pueden incluir estereotipos como `<<import>>` (importar elementos del paquete proveedor) o `<<access>>` (acceso directo a elementos).
****
#### **Notación**
Un paquete se muestra como un rectángulo grande con un rectángulo pequeño (una “*etiqueta*”) unido en una esquina (normalmente, la cima izquierda del rectángulo grande).
Pueden dibujarse flechas discontinuas entre los símbolos del paquete para mostrar las **relaciones**, indica que un paquete depende de otro porque sus elementos usan elementos del paquete destino.

![Pasted image 20250624212933.png](/assets/Pasted image 20250624212933.png)

**Más sobre relaciones entre paquetes.** **Importación**:

- Representada por una flecha punteada con el estereotipo `<<import>>`.
- Permite que los elementos de un paquete sean accesibles en otro.