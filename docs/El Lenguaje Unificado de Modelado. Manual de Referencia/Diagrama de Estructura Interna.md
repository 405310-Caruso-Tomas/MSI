![Pasted image 20250622174638.png](/MSI/assets/Pasted image 20250622174638.png)

Muestra la **descomposición de una clase**.

- Representa **la estructura interna de un [Clasificador](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Clasificador)** (clase o componente).

Un clasificador estructurado modela las partes de una clase y sus conectores contextuales. 
Una clase estructurada puede ser encapsulada forzando a que las comunicaciones desde el exterior pasen a través de los **puertos** cumpliendo con las interfaces declaradas.
****
###### **Problema**
La Figura 3.2 muestra el diagrama de estructura interna de la aplicación de la taquilla de teatro para el sistema de venta de entradas. Esta clase se descompone en tres partes: la **interfaz** del expendedor de entradas, una guía de representación, que recupera representaciones según la fecha u otro criterio, y un conjunto de bases de datos que contienen los datos de las representaciones y de las entradas. Cada parte interactúa con el exterior a través de un puerto. Lo mensajes sobre este puerto son enviados a la clase expendedor de entradas, pero la estructura interna de la clase taquilla está oculta de los clientes externos.