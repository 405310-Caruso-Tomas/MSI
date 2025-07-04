**[Clasificador](../../assets/Clasificador.md)** que representa una parte **modular** de un sistema, encapsulando un conjunto de **funcionalidades** o comportamientos específicos que se pueden **reutilizar**, **implementar** o **reemplazar** de manera independiente.

> Parte modular del diseño de un sistema que oculta su implementación tras un conjunto de inter faces externas.

Utilizados principalmente en un **[Diagrama de Componentes](../../assets/Diagrama de Componentes.md)**, para modelar la estructura física o lógica de un sistema, como módulos de software, bibliotecas, archivos, o subsistemas.
- **Encapsulación:** Un componente agrupa un conjunto de [Clases](../../assets/Clases.md), interfaces u otros elementos, exponiendo solo ciertas interfaces o **[Puerto](../../assets/Puerto.md)s** al exterior, ocultando los detalles internos. 
- **Ejemplo:** En el sistema de biblioteca, un componente `GestorPréstamos` podría implementar una interfaz `IPrestamo` con operaciones como `prestar()` y `devolver()`.
Encapsula **funcionalidad**, y está diseñado para ser reemplazable.
****
Los componentes tienen dos **aspectos**. Definen la apariencia externa de una pieza de un sistema e implementan dicha funcionalidad. Los componentes sin implementación son tipos **abstractos**. Se utilizan para especificar los requisitos de una ranura del sistema. Los componentes **con implementación** deben ser subtipos de un componente abstracto.
****
#### **Notación**
Un **componente** se representa como un rectángulo con el **[Estereotipo](../../assets/Estereotipo.md)** `<<component>>` o con un símbolo de componente (dos pequeños rectángulos sobresaliendo del lado izquierdo).
Dentro del rectángulo, se escribe el nombre del componente.
Puede incluir **[Puerto](../../assets/Puerto.md)s** (pequeños cuadrados en el borde) para definir puntos de interacción.
![Pasted image 20250623114511.png](../../assets/Pasted image 20250623114511.png.md)
En vez de la palabra clave, o además de ella, puede contener un icono de componente en su esquina superior derecha.