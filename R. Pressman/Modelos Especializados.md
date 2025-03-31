##### Modelo Concurrente
Permite que varias actividades (diseño, codificación, pruebas) ocurran simultáneamente, ajustándose según el estado del proyecto. 
Supongamos que tenemos la actividad de modelado, la cual se logra por medio de las siguientes acciones: hacer prototipos, análisis y diseño. Esta actividad puede estar en cualquiera de los estados de la imagen.

![[Pasted image 20250322142423.png]]

De esta forma, este modelo define una **Red del proceso**: Cada actividad existe en simultaneo con las demas. Los eventos generados en cierto punto de la red del proceso desencadenan: Los eventos generados en cierto punto de la red del proceso desencadenan transiciones entre los estados.
Por ejemplo, la actividad de comunicación (no se muestra en la figura) termina su primera iteración al principio de un proyecto y existe en el estado de cambios en espera. La actividad de modelado (que existía en estado inactivo mientras concluía la comunicación inicial, ahora hace una transición al estado en desarrollo. Sin embargo, si el cliente indica que deben hacerse cambios en los requerimientos, la actividad de modelado pasa del estado en desarrollo al de cambios en espera.

