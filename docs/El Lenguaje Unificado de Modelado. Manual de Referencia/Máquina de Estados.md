Si bien parece ser que una **máquina de estados** (modelo conceptual/lógica subyacente) difiere de lo que sería un **diagrama de estados** (representación del modelo conceptual), para este repositorio lo tomaremos como idénticos y se hará referencia a uno para indicar el otro y viceversa.
****
> Una **máquina de estados** es un grafo de estados y transiciones.

Modela las posibles historias de vida de un objeto de una **clase**, todos el conjunto de **estados** por los cuales pasa el objeto en respuesta a **eventos**. 
Una máquina de estados contiene estados conectados por transiciones. (**[Clases](../assets/Clases.md)**)
	![Pasted image 20250626120519.png](../assets/Pasted image 20250626120519.png.md)
Normalmente, una **máquina de estados** está vinculada a una clase, y describe la respuesta de una instancia de la clase a los eventos que recibe. 
Las máquinas de estados también se pueden vincular a comportamientos, **casos de uso** y **[Colaboración](../assets/Colaboración.md)es** para describir su ejecución.
![Pasted image 20250622110301.png](../assets/Pasted image 20250622110301.png.md)
- Los **estados** se representan como rectángulos con esquinas redondeadas. Cada estado modela un periodo de tiempo durante la vida de un objeto en el que satisface ciertas condiciones.
- Las **transiciones** son flechas etiquetadas con eventos y, opcionalmente, acciones o guardas. Llevan al objeto a un nuevo **estado**.
- Cuando se dispara una **transición**, se ejecuta un **efecto** (acción o actividad) asociada a la transición.
****
###### **Problema**
El estado inicial de una entrada (representado por un punto negro) es el estado **Disponible**. Antes de que comience la temporada, se asignan los asientos para los abonados de la temporada. Las entradas individuales adquiridas interactivamente se bloquean primero mientras los clientes realizan una selección. Después de esto, se venden o se liberan si son rechazadas. Si el cliente tarda demasiado tiempo en realizar la selección, finaliza el tiempo para la transacción y el asiento se libera. Los asientos vendidos a los abonados de la temporada se pueden cambiar para otras representaciones, en cuyo caso, vuelven a estar disponibles de nuevo.
****
###### **Más**
Este diagrama puede ser implementado mediante **estados anidados** y **estados compuestos.**
![Pasted image 20250626120617.png](../assets/Pasted image 20250626120617.png.md)