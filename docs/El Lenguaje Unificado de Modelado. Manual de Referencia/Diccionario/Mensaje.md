Transporte de información desde un rol a otro como parte de una **[Interacción](../../assets/Interacción.md)** dentro de un contexto; 
A nivel de instancia, **comunicación** desde un **objeto** a otro.
> Un **mensaje** es una representación de la comunicación entre objetos, roles o **[Clasificador](../../assets/Clasificador.md)es** en un sistema, modelando cómo interactúan para realizar una funcionalidad específica.

Un mensaje puede ser una señal o la llamada a una operación.
Se utiliza principalmente en **[Diagrama de Secuencia](../../assets/Diagrama de Secuencia.md)** y **[Diagrama de Comunicación](../../assets/Diagrama de Comunicación.md)** (o colaboración) para mostrar el intercambio de información, solicitudes de acciones o invocaciones de comportamientos.
También, la recepción de un **mensaje** puede desencadenar una transición de **[Máquina de Estados](../../assets/Máquina de Estados.md)**.
****
#### **Notación**
**Tipos de mensajes**:
- **Síncrono**: El emisor espera una respuesta (flecha llena: →).
- **Asíncrono**: El emisor no espera respuesta (flecha abierta: ➜).
- **Respuesta**: Retorno de un mensaje síncrono (flecha discontinua: -->).
- **Creación/Destrucción**: Indica la creación o eliminación de un objeto.
La notación para los diagramas de secuencia y de comunicación es diferente.
- En **[Diagrama de Secuencia](../../assets/Diagrama de Secuencia.md)**: Flechas entre líneas de vida de objetos, etiquetadas con el nombre del mensaje.
- En **[Diagrama de Comunicación](../../assets/Diagrama de Comunicación.md)**: Líneas etiquetadas con un número de orden (ejemplo: `1: realizarPedido()`).
