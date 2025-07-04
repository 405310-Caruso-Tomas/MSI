![Pasted image 20250622104322.png](../assets/Pasted image 20250622104322.png.md)
****
Las **[Clases](../assets/Clases.md)** se dibujan como **rectángulos**. La lista de atributos y operaciones se muestran en compartimentos separados.
Las [Relaciones](../assets/Relaciones.md) entre **clases** se muestran como las líneas que conectan los rectángulos de las clases. Los diferentes tipos de relaciones se distinguen por la textura de la línea y por los ador nos en las líneas o en sus extremos.
El **calificador** es un atributo (clave) que se coloca cerca de una clase asociada para indicar que **la selección de la instancia relacionada depende de un valor específico**.
- El diagrama de clases se puede representar gráficamente en forma abreviada, cuando no muestra atributos ni métodos.
****
###### **Problema**
La Figura 3.1 muestra un diagrama de clases de la aplicación de la taquilla del teatro. 
Muestra varias clases importantes, como `Cliente`, `Reserva`, `Entrada` y Representación. Los clientes pueden tener muchas reservas, pero cada reserva es hecha por un único cliente. Las reservas son de dos tipos: suscripción a un ciclo y reservas individuales. Ambos reservan entradas: en el primer caso varias entradas, mientras que en el segundo sólo una entrada. Cada entrada puede ser parte de una suscripción a un ciclo o de una reserva individual, pero no de ambos. Cada representación tiene muchas entradas disponibles, cada una con un único número de asiento. Una representación se puede identificar mediante la obra, la fecha y la hora.