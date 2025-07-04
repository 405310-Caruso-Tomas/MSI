> **Mecanismo** de extensión que permite personalizar o especializar elementos del modelo para adaptarlos a un contexto o dominio específico.

Se utiliza para añadir información adicional, semántica o restricciones a elementos UML existentes (como **clases**, **asociaciones**, **componentes**, etc.) sin modificar la estructura básica del lenguaje.

Un elemento estereotipado puede tener restricciones más allá de aquéllos del elemento base, así como una imagen visual distinta y propiedades adicionales definidos a través de **[Valores Etiquetados](../../assets/Valores Etiquetados.md)**.
Los estereotipos suelen definirse en un **[Perfil](../../assets/Perfil.md)** UML, que es un conjunto de extensiones para un dominio o propósito específico.

 **Ejemplo**: En un sistema de biblioteca, una clase Libro podría estereotiparse como `<<Persistent>>` para indicar que sus instancias se almacenan en una base de datos. Se aplican a cualquier diagrama UML.
****
#### **Notación**
Se representa entre **guillemets** (`<< >>`), como `<<entity>>`, `<<controller>>` o `<<interface>>`, y se coloca generalmente encima o junto al nombre del elemento al que aplica.
![Pasted image 20250623130158.png](../../assets/Pasted image 20250623130158.png.md)

