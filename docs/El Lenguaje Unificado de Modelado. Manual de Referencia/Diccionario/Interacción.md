Una **interacción** es un concepto que describe el **comportamiento** **dinámico** de un sistema mediante el intercambio de **[Mensaje](../../assets/Mensaje.md)s** entre **objetos**, **roles** o **[Clasificador](../../assets/Clasificador.md)es** (como **[Clases](../../assets/Clases.md)**, [Componente](../../assets/Componente.md)s o **actores**) en un contexto específico, como un **[Caso de Uso](../../assets/Caso de Uso.md)** o un escenario.

> Especificación de cómo se intercambian los **mensajes** a lo largo del tiempo entre **roles** dentro de un contexto para realizar una tarea.

- Utilizadas para modelar cómo los **elementos** colaboran para lograr un objetivo, enfocándose en la **secuencia**, el **flujo** y las **condiciones** de sus **comunicaciones**.
- Una secuencia de **mensajes** (comunicación entre objetos) dentro de una **[Colaboración](../../assets/Colaboración.md)** que implementan un comportamiento se denomina **interacción**.
- **Encapsulación**: Puede definirse dentro de un **clasificador** (como un componente) o en una **colaboración**, que agrupa roles e interacciones para un propósito común.
- Un **rol** es una ranura que debe ser rellenada con objetos en un uso concreto de una interacción.
****
Las interacciones se modelan principalmente en los siguientes diagramas, conocidos como **diagramas de interacción**:
1. **[Diagrama de Secuencia](../../assets/Diagrama de Secuencia.md)**: Muestra el orden temporal de los **mensajes** entre líneas de vida, enfatizando la secuencia de eventos.
    - Ejemplo: Un cliente envía un mensaje `realizarPedido()` a un sistema, que responde tras verificar el inventario.
2. **[Diagrama de Comunicación](../../assets/Diagrama de Comunicación.md)** (o colaboración): Enfoca la estructura de las interacciones, mostrando los roles y los mensajes con un número que indica el orden.
    - Ejemplo: `:Cliente` conectado a `:SistemaPedidos` con un mensaje etiquetado `1: realizarPedido()`.