Una **interacción** es un concepto que describe el **comportamiento** **dinámico** de un sistema mediante el intercambio de **[Mensaje](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Mensaje)s** entre **objetos**, **roles** o **[Clasificador](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Clasificador)es** (como **[Clases](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Clases)**, [Componente](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Componente)s o **actores**) en un contexto específico, como un **[Caso de Uso](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Caso de Uso)** o un escenario.

> Especificación de cómo se intercambian los **mensajes** a lo largo del tiempo entre **roles** dentro de un contexto para realizar una tarea.

- Utilizadas para modelar cómo los **elementos** colaboran para lograr un objetivo, enfocándose en la **secuencia**, el **flujo** y las **condiciones** de sus **comunicaciones**.
- Una secuencia de **mensajes** (comunicación entre objetos) dentro de una **[Colaboración](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Colaboración)** que implementan un comportamiento se denomina **interacción**.
- **Encapsulación**: Puede definirse dentro de un **clasificador** (como un componente) o en una **colaboración**, que agrupa roles e interacciones para un propósito común.
- Un **rol** es una ranura que debe ser rellenada con objetos en un uso concreto de una interacción.
****
Las interacciones se modelan principalmente en los siguientes diagramas, conocidos como **diagramas de interacción**:

1. **[Diagrama de Secuencia](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Secuencia)**: Muestra el orden temporal de los **mensajes** entre líneas de vida, enfatizando la secuencia de eventos.
    
	- Ejemplo: Un cliente envía un mensaje `realizarPedido()` a un sistema, que responde tras verificar el inventario.
2. **[Diagrama de Comunicación](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Comunicación)** (o colaboración): Enfoca la estructura de las interacciones, mostrando los roles y los mensajes con un número que indica el orden.
    
	- Ejemplo: `:Cliente` conectado a `:SistemaPedidos` con un mensaje etiquetado `1: realizarPedido()`.