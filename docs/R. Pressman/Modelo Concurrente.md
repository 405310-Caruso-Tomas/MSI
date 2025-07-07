> Permite que varias **actividades** (**diseño**, **codificación**, **pruebas**) ocurran simultáneamente, ajustándose según el estado del **[Proyecto](/MSI/PMBOK/Proyecto)**. 
****

Supongamos que tenemos la actividad de **[Modelado](/MSI/Patrones en la Construcción de Modelos Conceptuales para Sistemas de Información/Modelado)**, la cual se logra por medio de las siguientes acciones: **hacer** **prototipos**, **análisis** y **diseño**. 
Esta actividad puede estar en cualquiera de los estados de la imagen.

![Pasted image 20250322142423.png](/MSI/assets/Pasted image 20250322142423.png)

De esta forma, este modelo define una **Red del proceso**:

- Cada actividad existe en simultaneo con las demás. Los eventos generados en cierto punto de la red del proceso desencadenan transiciones entre los **estados**.

**Por ejemplo**, la actividad de **comunicación** (no se muestra en la figura) termina su primera **iteración** al principio de un **proyecto** y existe en el estado de cambios en espera. La actividad de modelado (que existía en estado inactivo mientras concluía la comunicación inicial, ahora hace una transición al estado en desarrollo. Sin embargo, si el cliente indica que deben hacerse cambios en los **[Requerimientos](/MSI/Patrones en la Construcción de Modelos Conceptuales para Sistemas de Información/Requerimientos)**, la actividad de **modelado** pasa del estado en *desarrollo* al de *cambios en espera*.
****

