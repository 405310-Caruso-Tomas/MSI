Transporte de información desde un rol a otro como parte de una **[Interacción](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Interacción)** dentro de un contexto; 
A nivel de instancia, **comunicación** desde un **objeto** a otro.

> Un **mensaje** es una representación de la comunicación entre objetos, roles o **[Clasificador](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Clasificador)es** en un sistema, modelando cómo interactúan para realizar una funcionalidad específica.

Un mensaje puede ser una señal o la llamada a una operación.
Se utiliza principalmente en **[Diagrama de Secuencia](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Secuencia)** y **[Diagrama de Comunicación](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Comunicación)** (o colaboración) para mostrar el intercambio de información, solicitudes de acciones o invocaciones de comportamientos.
También, la recepción de un **mensaje** puede desencadenar una transición de **[Máquina de Estados](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Máquina de Estados)**.
****
#### **Notación**
**Tipos de mensajes**:

- **Síncrono**: El emisor espera una respuesta (flecha llena: →).
- **Asíncrono**: El emisor no espera respuesta (flecha abierta: ➜).
- **Respuesta**: Retorno de un mensaje síncrono (flecha discontinua: -->).
- **Creación/Destrucción**: Indica la creación o eliminación de un objeto.

La notación para los diagramas de secuencia y de comunicación es diferente.

- En **[Diagrama de Secuencia](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Secuencia)**: Flechas entre líneas de vida de objetos, etiquetadas con el nombre del mensaje.
- En **[Diagrama de Comunicación](/MSI/El Lenguaje Unificado de Modelado. Manual de Referencia/Diagrama de Comunicación)**: Líneas etiquetadas con un número de orden (ejemplo: `1: realizarPedido()`).
