> Implementación física de un elemento del modelo como un artefacto.

Un **[Artefacto](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Artefacto)** puede ser una **manifestación** (es decir, una implementación) de un componente.
La **manifestación** es una relación que conecta un **artefacto** físico con un elemento lógico del diseño.

- La relación de **manifestación** indica que un **artefacto** "da vida" a un componente, implementando sus interfaces y comportamiento. 
- Se utiliza principalmente en [Diagrama de Despliegue](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Despliegue) para conectar el mundo lógico (diseño del software) con el mundo físico (archivos o productos concretos que se despliegan en nodos).
- **Dirección:** La **manifestación** va del artefacto al **[Clasificador](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Clasificador)** (el artefacto "manifiesta" o implementa el clasificador).
****
##### **Notación**
Una **relación** de **manifestación** se representa con una flecha de dependencia, una línea discontinua con una cabeza de flecha sencilla, desde un artefacto a un elemento del modelo.
Se coloca la palabra clave `<<manifest>>` en la flecha.

![Pasted image 20250623190855.png](/MSI/assets/Pasted image 20250623190855.png)