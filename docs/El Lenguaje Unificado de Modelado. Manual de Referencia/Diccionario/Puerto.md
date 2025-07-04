**Punto de interacción.** Especifica un lugar donde el **[Clasificador](../../assets/Clasificador.md)** intercambia mensajes, datos o servicios con el exterior.

> Punto de conexión entre un clasificador y su entorno. Las conexiones del mundo externo se hacen a los puertos según sean requeridos por las **interfaces** declaradas en un puerto.

**Interfaz Asociada.** El comportamiento de un puerto se especifica por sus interfaces **proporcionadas** e interfaces **requeridas**. Pueden verse estas dos en un **[Diagrama de Componentes](../../assets/Diagrama de Componentes.md)**, donde son comunes los puertos.
- Definen un punto de entrada/salida en una clase. Ejemplo: En el sistema de biblioteca, la clase `SistemaBiblioteca` podría tener un puerto `InterfazUsuario` que expone operaciones como `prestarLibro()`
****
#### **Notación**
Puertos declarados en [Diagrama de Estructura Interna](../../assets/Diagrama de Estructura Interna.md):
Un puerto se muestra como un cuadrado pequeño que monta el límite de un rectángulo del clasificador.
El nombre del puerto se pone cerca del cuadrado. El cuadrado puede ponerse en el interior del rectángulo del clasificador para indicar un puerto con visibilidad restringida, como un puerto de servicio; éstos deben ser raros, porque el propósito principal de los puertos es encapsular comunicación con el ambiente. 
El tipo de un puerto puede mostrarse siguiendo una coma, usando la sintaxis: `nombre: Tipo[multiplicidad]`.
En lugar de declarar el puerto por tipos, pueden mostrarse las interfaces para el puerto usando símbolos de la interfaz.
![Pasted image 20250623104502.png](../../assets/Pasted image 20250623104502.png.md)