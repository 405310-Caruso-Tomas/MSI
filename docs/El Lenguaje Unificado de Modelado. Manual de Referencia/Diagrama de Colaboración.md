Una **[Colaboración](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Colaboración)** es una relación contextual entre un conjunto de objetos que trabajan juntos para lograr un propósito. 

![Pasted image 20250622105312.png](/MSI/assets/Pasted image 20250622105312.png)

Contiene una colección de **roles** dentro de un patrón genérico, que pueden ser representadas por objetos individuales, o vinculadas a ellos. 
****
##### **Problema**
La Figura 3.3 muestra un diagrama de colaboración para el sistema de venta del teatro. En él interactúan tres tipos distintos de componentes para proporcionar la funcionalidad al sistema: quiosco, terminales de ventas y la aplicación de la taquilla. 

Los diferentes componentes no pertenecen a una única clase global, sino que cooperan de maneras bien definidas para ofrecer servicios a los usuarios.
****
##### **Discrepancias**
Para este diagrama en particular, hay diferencias con respecto a lo dictado en el apunte teórico y el Manual de Referencia UML, por lo que se describe a continuación la otra cara de lo que sería un **diagrama de colaboración**.

Este diagrama muestra como los **objetos** y los **[Actor](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Actor)es** intercambian mensajes y **colaboran** entre sí para cumplir el objetivo de un **[Caso de Uso](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Caso de Uso)**. Es decir, ambas perspectivas concuerdan en que el diagrama representa **[Interacción](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Interacción)es**.

Se utilizan tres tipos de clases: de entidad, de interfaz y de control.

![Pasted image 20250626115452.png](/MSI/assets/Pasted image 20250626115452.png)

Este diagrama es el modelo lógico para representar el concepto del **Modelo vista controlador. (MVC)**, veamos el ejemplo:

![Pasted image 20250626115701.png](/MSI/assets/Pasted image 20250626115701.png)

