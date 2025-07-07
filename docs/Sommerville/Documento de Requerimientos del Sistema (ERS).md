> Tiene que definir con exactitud lo que se implementará, ya que **es un comunicado oficial de lo que se debe implementar.** 

- Puede formar parte del contrato entre el comprador del sistema y los desarrolladores del software. 
- **Incluye tanto los requerimientos del usuario para un sistema, como una especificación detallada de los requerimientos del sistema.**

> Son esenciales los documentos de requerimientos cuando un contratista externo diseña el sistema de software. Sin embargo, los métodos de desarrollo ágiles argumentan que los requerimientos cambian tan rápidamente que un documento de requerimientos se vuelve obsoleto tan pronto como se escribe. En lugar de un documento formal, los enfoques como la programación extrema (Beck, 1999) recopilan de manera incremental requerimientos del usuario y los escriben en tarjetas como historias de usuario. 

Si se utiliza un proceso de desarrollo iterativo interno, entonces el documento de requerimientos suele ser mucho menos detallado y cualquier ambigüedad puede resolverse durante el desarrollo del sistema.

El documento de requerimientos ***no debe incluir detalles de la arquitectura o el diseño del sistema***. Este documento suele tener un conjunto variado de usuarios, por lo que es interpretado desde diferentes perspectivas:

![Pasted image 20250401094747.png](/MSI/assets/Pasted image 20250401094747.png)

El nivel de detalle incluido depende del tipo de sistema a diseñar y el proceso de desarrollo utilizado.
****
#### **Notaciones**
Debe escribir los requerimientos del usuario en lenguaje natural, con formas sencillas, diagramas intuitivos. A su vez, los requerimientos del sistema se escriben también en lenguaje natural, pero de igual modo se utilizan otras notaciones:

![Captura de pantalla de 2025-04-01 09-26-44.png](/MSI/assets/Captura de pantalla de 2025-04-01 09-26-44.png)

Los modelos gráficos, como [UML](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/UML) son más útiles cuando es necesario mostrar cómo cambia un estado o al describir una secuencia de acciones.
****
##### **Especificación en Lenguaje Natural**
Desde los albores de la ingeniería de software, el lenguaje natural se usa para escribir los requerimientos de software. Para minimizar la ambigüedad, se recomienda: 

1. Elaborar un formato estándar y asegurarse de que todas las definiciones de requerimientos se adhieran a dicho formato.

2. Utilizar el lenguaje de manera clara para distinguir entre requerimientos obligatorios y deseables. Los primeros con "debe ser", y los segundos con "debería ser".

3. Usar texto resaltado para partes clave del requerimiento.

4. Evitar el uso de lenguaje técnico. No deduzca que los lectores entienden de ingeniería de software.

5. Siempre que sea posible, asocie una razón con cada requerimiento de usuario. El por qué se incluyó dicho requerimiento.
##### **Especificaciones Estructuradas**
El lenguaje natural estructurado es una manera de escribir requerimientos del sistema, donde está **limitada la libertad del escritor**

![Pasted image 20250401094047.png](/MSI/assets/Pasted image 20250401094047.png)

Cuando use una forma estándar para especificar requerimientos funcionales, debe
incluir la siguiente información:

1. Una descripción de la función o entidad a especificar.
2. Una descripción de sus entradas y sus procedencias.
3. Una descripción de sus salidas y a dónde se dirigen.
4. Datos requeridos para el cálculo/acción.
5. Descripción de la acción que se va a tomar.
6. Una precondición que establece lo que debe ser verdadero antes de llamar a la función, y una postcondición que especifica lo que es verdadero después de llamar a la función.
7. Efectos colaterales.
****

#### **Estructura para el documento basado en Estándar IEEE, 1998**
Capítulos:

- **Prefacio**: Debe definir el número esperado de lectores del documento, así como describir su historia de versiones, junto con sus causas y cambios realizados.
- **Introducción**: Describe las funciones del sistema y cómo funcionará con otros sistemas, además de cómo se ajusta con objetivos empresariales o estratégicos de la organización que comisiona el software.
- **Glosario**: Define los términos técnicos usados en el documento.
- **Definición** **de** **requerimientos** **del** **usuario**: Aquí se representan los servicios que ofrecen al usuario. Requerimientos no funcionales del sistema. Esta descripción puede usar lenguaje natural, diagramas u otras observaciones que sean comprensibles para los clientes.
- **Arquitectura** **del** **sistema**: Panorama de alto nivel de la arquitectura anticipada del sistema, destacando los componentes arquitectónicos que sean de reutilización.
- **Especificación** **de** **requerimientos** del sistema: Debe representar los requerimientos funcionales y no funcionales con más detalle.
- **Modelos** **del** **sistema**: modelos gráficos del sistema que muestren las relaciones entre componentes del sistema, el sistema y su entorno. Algunos especificados en [Metodologías de Modelado](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Metodologías de Modelado)
- **Evolución del sistema**: Describe los supuestos fundamentales sobre los que se basa el sistema, y cualquier cambio anticipado debido a hardware, necesidades del usuario, etc. Esta sección es útil para los diseñadores del sistema, pues los ayuda a evitar decisiones de diseño que restringirían probablemente futuros cambios al sistema.
- **Apéndices**: Brindan información específica y detallada que se relaciona con la aplicación a desarrollar. Requisitos de hardware (configuración mínima y óptima) y bases de datos (organización lógica y relaciones entre datos).
- **Índice**: Puede ser un índice alfabético normal, uno de diagramas, un índice de funciones, etcétera.

Hay distintas versiones respecto a lo que debe incluir la ERS según el estándar IEEE, es por ello que se adjunta otro modelo propuesto (*apunte teórico*):

![Pasted image 20250702205842.png](/MSI/assets/Pasted image 20250702205842.png)

