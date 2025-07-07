El enfoque más utilizado del **desarrollo** de software **ágil**. 
> Aunque las primeras actividades con las ideas y los métodos asociados a **XP** ocurrieron al final de la década de 1980, el trabajo fundamental sobre la materia había sido escrito por *Kent Beck*. 

![Pasted image 20250702113211.png](/MSI/assets/Pasted image 20250702113211.png)

*Beck* define un conjunto de **cinco valores** que establecen los fundamentos para todo trabajo realizado como parte de **XP**:

- **Comunicación.** Colaboración estrecha pero informal entre clientes y desarrolladores.
- **Simplicidad.** Diseño de necesidades inmediatas, y no las del futuro. Si es necesario refactorizar, se hará más adelante.
- **Retroalimentación.** 
- **Valentía** para diseñar para hoy y reconocer que los [Requerimientos](/MSI/Patrones en la Construcción de Modelos Conceptuales para Sistemas de Información/Requerimientos) futuros tal vez cambien mucho.
- **Respeto.** Conforme a los participantes y al proceso.
****
Este modelo usa un **[Enfoque Orientado a Objetos](/MSI/R. Pressman/Enfoque Orientado a Objetos)** como paradigma de desarrollo, y engloba cuatro actividades estructurales.
#### **Planeación (Juego de Planeación)** 

- Los clientes escriben [Historias de Usuario](/MSI/Users Stories Applied - Mike Cohn/Historias de Usuario) y les asignan un valor de prioridad. Luego, los miembros del equipo evalúan cada historia y le asignan un costo, medido en semanas de desarrollo. Se puede pedir al cliente que descomponga la historia en más chicas. En cualquier momento es posible escribir o modificar nuevas historias.
- Los **clientes** y **desarrolladores** trabajan juntos para decidir cómo agrupar las **historias** en el siguiente incremento a desarrollar.
- Se llega a un **compromiso** sobre la entrega, y cuando esta ocurre se calcula la **velocidad** del [Proyecto](/MSI/PMBOK/Proyecto) y se planifican próximas entregas en base a la velocidad.
#### **Diseño**

- XP estimula el uso de tarjetas CRC (tarjetas que representan **[Clases](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Clases)** cada una, sus responsabilidades y colaboradores {[Colaboración](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Colaboración)}, donde los colaboradores son otras clases con las que interactúa la clase de la tarjeta) para pensar en el software orientado a objetos.
- Si en el diseño de una historia se encuentra un problema de diseño difícil, XP recomienda la creación inmediata de un **prototipo** para esa porción del diseño. Esto se conoce como **solución en punta**.
- Debido a que esta etapa de **diseño** genera pocos productos del trabajo que no sean tarjetas **CRC** o **soluciones** **en** **punta**, el **diseño** es visto como un **[Artefacto](/El Lenguaje Unificado de Modelado. Manual de Referencia/Diccionario/Artefacto)** en **construcción** que puede y **debe** **modificarse** **continuamente** a medida que avanza la construcción.
#### **Codificación** 

- No se comienza a construir el producto sin antes realizar **[Pruebas Unitarias](/MSI/A Software Testing Primer - Nick Jenkins/Pruebas Unitarias)** a cada una de las historias que se van a incluir en el **incremento**.
- Una vez creada la prueba unitaria, el desarrollador está mejor capacitado para centrarse en lo que debe implementarse para pasar la prueba. No se agrega nada extraño, siguiendo el valor de la **simplicidad**.
- XP recomienda que dos personas trabajen juntas en una estación de trabajo con el objeto de crear código para una historia, esto es la **programación por parejas**. **_"Dos cabezas piensan mejor que una"._**
- A medida que las parejas terminan su trabajo, este se integra con el de los demás, ayudando a evitar los problemas de compatibilidad e interfaces.
#### **Pruebas** 

- Las pruebas unitarias que se crean deben implementarse con el uso de una estructura que permita automatizarlas ([Pruebas Automatizadas](/MSI/A Software Testing Primer - Nick Jenkins/Pruebas Automatizadas)). Esto estimula una estrategia de **pruebas de regresión** ([Enfoques de Testing](/MSI/A Software Testing Primer - Nick Jenkins/Enfoques de Testing)) siempre que se modifique el código. **_"Corregir pequeños problemas cada cierto número de horas toma menos tiempo que resolver problemas enormes justo antes del plazo final."._**
- Las **[Pruebas de Aceptación](/MSI/A Software Testing Primer - Nick Jenkins/Pruebas de Aceptación)** XP, son especificadas por el cliente y derivan de las historias de usuario ya implementadas.