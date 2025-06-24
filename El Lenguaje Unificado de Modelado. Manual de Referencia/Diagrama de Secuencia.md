> Tipo de diagrama de interacción que muestra cómo los objetos intercambian **[[Mensaje]]s** en un sistema durante un **[[Caso de Uso]]** específico, enfatizando el orden temporal de estas interacciones.

Muestra una **[[Interacción]]** como un gráfico de dos dimensiones. La dimensión vertical es el eje de tiempo, de arriba hacia abajo. Los mensajes más altos ocurren antes que los más bajos.
Un [[Mensaje]] se muestra como una flecha desde la línea de vida de un objeto a la línea de vida del otro.
****
##### **Estructura general**
- En la parte superior, se colocan los **actores** u **objetos** participantes. Las entidades que interactúan, y se dibujan como rectángulos en la parte superior del diagrama.
- Las líneas de vida se extienden hacia abajo desde cada objeto.
- Las flechas de **mensajes** conectan las líneas de vida, mostrando la secuencia de **interacciones**.
Cada **rol** se representa mediante una columna vertical que contiene un símbolo de cabecera y una línea de vida vertical. Durante el tiempo que existe un objeto, la línea de vida se representa con una línea discontinua. Durante el tiempo que la ejecución de una acción sobre el objeto está activa, la línea de vida se representa con una línea doble.
![[Pasted image 20250623205659.png]]
La imagen adjunta muestra un diagrama de secuencia típico con mensajes asíncronos, pero tener en cuenta que los **[[Mensaje]]s** pueden ser de cualquier tipo.
****
**Fragmentos combinados**:
- Estructuras que agrupan **mensajes** para mostrar **condiciones**, **bucles** o **interacciones** opcionales:
    - **alt**: Alternativa (similar a un "*if-else*").
    - **opt**: Opcional (algo que puede o no ocurrir).
    - **loop**: Bucle (repetición de mensajes).
    - **par**: Paralelo (mensajes que ocurren simultáneamente).
![[Pasted image 20250623210422.png]]